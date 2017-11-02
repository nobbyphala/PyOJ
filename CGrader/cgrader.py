import signal
import difflib
import filecmp
import json
from time import gmtime, strftime

from cmd import *

def compile(filep):

    stime = strftime("%H%M%S", gmtime())
    execCommand = "gcc {} -o /tmp/{}"
    outNameFile = "cgrader"+stime

    execCommand = execCommand.format(filep,outNameFile)

    res = subprocess_cmd(execCommand)

    if res==0:
        return (True,"/tmp/"+outNameFile)
    else:
        return (False, res)

def runTestCase(dirpath, execpath):
    opti = {}

    with open(dirpath+"options.json") as json_data:
        opti = json.load(json_data)
        json_data.close()


    outputPath = dirpath+"tmp/{}.out"
    inputPath = dirpath+"{}.in"
    outComparePath = dirpath+"{}.out"

    numTestCase = opti["TestCase"]
    execCommand = "{} < {} > {}"

    testresult={}

    for i in range(1,numTestCase+1):
        cmd = execCommand.format(execpath,inputPath.format(i), outputPath.format(i))
        ret = subprocess_cmd(cmd)

        if(ret == 0):
            if(filecmp.cmp(outputPath.format(i), outComparePath.format(i))):
                testresult[i] = "accepted"
            else:
                testresult[i] = "wrong answer"

        else:
            testresult[i] = "runtime error"

    return testresult
