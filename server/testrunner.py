import asyncio

class Test(object):
    def __init__(self, id, command):
        self.id         = id
        self.command    = command
        self._process   = None
        self._status    = None
        self._pass_rate = None
        self._parsed    = False

    def finished(self):
        return (self._process != None and
                self._process.returncode != None)

    async def run(self):
        try:
            process_arguments = self.command.split(' ')
            self._process = await asyncio.create_subprocess_exec(
                *process_arguments, stdout=asyncio.subprocess.PIPE)
            self._status = 'running'
        except:
            self._status = 'error'

    async def status(self):
        await self._try_parse_output()
        return self._status

    async def pass_rate(self):
        await self._try_parse_output()
        return self._pass_rate

    async def _try_parse_output(self):
        if self.finished() and not self._parsed:
            await self._parse_output()

    async def _parse_output(self):
        process = self._process
        while not process.stdout.at_eof():
            byte_line = await process.stdout.readline()
            print(byte_line.decode('utf-8').replace('\n', ''))
        self._parsed = True
        # TODO: Fill status and pass_rate
        self._status    = 'failed'
        self._pass_rate = '5/10'


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
