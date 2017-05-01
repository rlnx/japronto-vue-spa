import re
import asyncio
import os.path
from config import config

class TestParser(object):
    regexp_passed = re.compile(r'.*Passed *:? *(?P<num>\d+).*')
    regexp_failed = re.compile(r'.*Failed *:? *(?P<num>\d+).*')

    def __init__(self):
        self.passed = None
        self.failed = None

    def parse(self, line):
        passed = self._match_regexp(TestParser.regexp_passed, line)
        failed = self._match_regexp(TestParser.regexp_failed, line)
        if not passed is None: self.passed = passed
        if not failed is None: self.failed = failed

    def _match_regexp(self, regexp, line):
        match = regexp.match(line)
        return int(match.group('num')) if match else None

class Test(object):
    def __init__(self, id, command):
        self.id         = id
        self.command    = command
        self._process   = None
        self._status    = None
        self._pass_rate = None
        self._parsed    = False
        self._error     = None

    def finished(self):
        return ( self._process != None and
                 self._process.returncode != None or
                 self._error )

    async def run(self):
        try:
            fixed_command = self._fix_command(self.command)
            self._process = await asyncio.create_subprocess_shell(
                fixed_command, stdout=asyncio.subprocess.PIPE)
        except Exception as ex:
            self._error     = ex
            self._pass_rate = 'N/A'
            self._status    = 'failed'

    async def status(self):
        await self._try_parse_output()
        return self._status

    async def pass_rate(self):
        await self._try_parse_output()
        return self._pass_rate

    async def _try_parse_output(self):
        if self.finished() and not self._parsed and not self._error:
            await self._parse_output()

    async def _parse_output(self):
        process = self._process
        parser  = TestParser()
        while not process.stdout.at_eof():
            byte_line = await process.stdout.readline()
            line      = byte_line.decode('utf-8')
            parser.parse(line)
        self._parsed = True
        self._status    = self._format_status(parser.passed, parser.failed)
        self._pass_rate = self._format_pass_rate(parser.passed, parser.failed)

    def _format_status(self, passed, failed):
        if failed is None or passed is None:
            return 'unknown'
        return 'failed' if failed > 0 else 'passed'

    def _format_pass_rate(self, passed, failed):
        if passed is None or failed is None:
            return 'N/A'
        return '{}/{}'.format(passed, passed + failed)

    def _fix_command(self, command):
        command_chunks = command.split(' ')
        if config.run_tests_scipt in command_chunks:
            command_chunks.insert(0, 'cd ' + config.test_dir + ' &&')
        return ' '.join(command_chunks)


class TestRunner(object):
    def __init__(self):
        self._tests = []

    async def schedule_test(self, id, command):
        test = Test(id, command)
        self._tests.append(test)
        await test.run()

    def finished_tests(self):
        remaning_tests = []
        finished_tests = []
        for test in self._tests:
            if test.finished():
                finished_tests.append(test)
            else:
                remaning_tests.append(test)
        self._tests = remaning_tests
        return finished_tests

test_runner = TestRunner()
