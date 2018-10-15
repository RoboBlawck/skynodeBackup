#Simple method which compresses files via a command line
import subprocess
from var import *


def zip(input, output):
    cmd = exe + " " + conf + " " + localpath+output + " " + " ".join(map(lambda x: localpath+x, input))
    print("Executing CMD:" + " " + cmd)
    sp = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    sp.communicate() #Todo: enable communication