
import os, sys


class DelimitedTextImportTest:


    def __init__(self, argsDict):
        print >>sys.stderr, '    test arguments:'
        for (k, v) in argsDict:
            print >>sys.stderr, '    ', k, ' = ', v


    def Execute(self):

        raise Exception('test failed by exception')


def newTestObject(argsDict):
    return DelimitedTextImportTest(argsDict)
