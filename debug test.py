#! python3

import os
import sys
import subprocess

if __name__ == '__main__':
    if os.path.isfile("config.txt"):
        prefference_file = open("config.txt")
    else:
        subprocess.call("exit 1", shell=False)
        sys.exit()
    prefference_file.close()
