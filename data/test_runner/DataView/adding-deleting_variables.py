import os, sys

class AddingDeletingVarsTest:
    def __init__(self, argsDict):
        print >>sys.stderr, '    test arguments:'
        for (k, v) in argsDict:
            print >>sys.stderr, '    ', k, ' = ', v

    def Execute(self):
        return 1


def newTestObject(argsDict):
    return AddingDeletingVarsTest(argsDict)
