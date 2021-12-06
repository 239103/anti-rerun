#!/usr/bin/env python

import subprocess, os

if __name__ == "__main__":
    proc = subprocess.Popen(["pgrep", "-f", __file__], stdout=subprocess.PIPE)
    std = proc.communicate()
    if len(std[0].decode().split()) > 1:
        exit('Already running')

    os.system("sleep 1000")
