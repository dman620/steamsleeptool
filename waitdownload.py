#! python3
#this script will only run in windows.
#it is tested in only Windows 10, though it should run with any version
#in which the windows commands I use are still valid and obviously for which
#steam is compatible
import time
import os
import sys
import subprocess



if __name__ == '__main__':
    if os.path.isfile("config.txt"):
        prefference_file = open("config.txt")
    else:
        print('error, config file does not exist.')
        print('You must create config.txt in this directory like this:')
        print('line 1: type your steam directory.  keep spaces, no quotes.')
        print('line 2: type either \"sleep\" or \"shutdown\" to change your prefference.')
        sys.exit()

    #load steam directory
    steam_directory = prefference_file.readline().rstrip()
    download_directory = steam_directory + '\steamapps\downloading'

    #load prefferences
    actionprefference = prefference_file.readline().rstrip()
    
    while(os.listdir(download_directory) != []):
        time.sleep(600)
        print('download not complete yet')
    print('download complete!')

    if actionprefference == 'shutdown':
        #this shuts the computer down
        subprocess.call("Shutdown.exe -s -t 00", shell=False)
    else:
        #this sleeps the computer
        subprocess.call("rundll32.exe powrprof.dll,SetSuspendState 0,1,0", shell=False)


    
    prefference_file.close()
