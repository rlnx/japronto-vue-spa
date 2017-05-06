import os, sys

class DataViewGridTest:
    def __init__(self, argsDict):
        print >>sys.stderr, '    test arguments:'
        for (k, v) in argsDict:
            print >>sys.stderr, '    ', k, ' = ', v

    def Execute(self):
        return 0

def newTestObject(argsDict):
    return DataViewGridTest(argsDict)
