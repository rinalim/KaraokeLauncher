#!/usr/bin/python

import os, sys, time
from subprocess import *

def run_cmd(cmd):
    # runs whatever in the cmd variable
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

def is_running(pname):
    ps_grep = run_cmd("ps -ef | grep " + pname + " | grep -v grep")
    if len(ps_grep) > 1 and "bash" not in ps_grep:
        return True
    else:
        return False

while True:
    if is_running("VideoKaraoke.jar") == True:
        break
    else:
        time.sleep(1)    # wait for launching jar

while True:
    if is_running("VideoKaraoke.jar") == False:
        sys.exit(0)
    else:
        time.sleep(1)    # wait for stopping jar