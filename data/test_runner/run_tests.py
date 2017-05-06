import imp
import os
import os.path
import sys
import xml.etree.ElementTree as ET

_passed = 0
_failed = 0

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("Log.txt", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
sys.stdout = Logger()
sys.stderr = sys.stdout

def get_module_name(filename):
    filename = os.path.basename(filename)
    filename = os.path.splitext(filename)[0]
    return filename

def run_tests(xmlfile):
    global _passed
    global _failed

    root = ET.parse(xmlfile).getroot()

    for task in root:
        task_name = ''
        task_args = {}

        if 'name' in task.attrib:
            task_name = task.attrib['name']
        args = task[0]

        test_path = ''
        for arg in args:
            name = arg.attrib['name']
            task_args[name] = arg.text
            if name == 'test_file_path':
                test_path = eval(arg.text.replace('?PACKAGE_PATH + "', '".'))

                if os.path.sep == '/':
                    test_path = test_path.replace('\\', '/')

        print 'TEST:', task_name
        print '========== OUTPUT =========='

        mod = imp.load_source(get_module_name(test_path), test_path)

        test_obj = mod.newTestObject(task_args.items())
        print '========== RESULT =========='
        res_code = 1

        try:
            res_code = test_obj.Execute()
        except:
            pass
        if res_code == 0 or res_code == None:
            print 'PASS'
            _passed += 1
        else:
            print 'FAIL'
            _failed += 1
        print ''

def find_xmls():
    for entry in os.listdir('.'):
        if os.path.isfile(entry) and \
        os.path.splitext(entry)[1].lower() == '.xml':
            run_tests(entry)

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        run_tests(sys.argv[1])
    else:
        find_xmls()

    print '========= SUMMARY =========='
    print 'Passed:', _passed
    print 'Failed:', _failed
