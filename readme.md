##HELLO THIS IS MY README

Version 1.0

Windows  10, Python3 used

###What is it:

It is a Python script, which will sleep or shutdown your computer whenever your steam games are finished downloading.  You can change that in the config file.

###How it works:

This program takes advantage of Steam's "downloading" folder, which stores temporary files in it while a download is happening.  It simply monitors this folder and sleeps/shuts down your computer once it is empty (i.e. once the download is finished)

###Why should you use:

Of course automation is better!  You can activate this script and go to the pool, and you can rest assured that you will not waste any electricity, or wear on your computer!  Of course the difference is probably minimal, but it always bothered me that I had to leave my computer on for the whole night just to download one 9GB game.

###Tested for:

This is currently only built on Windows.  Tested on Windows 10 and made with Python3.  Though it should work for any windows version for which the commands I use are still functional, and obviously for which Steam is still compatible.  It is such a short program that you can easily adapt it for other operating systems or versions.  I also may do this in the future.

###Setup:

This comes with a "config.txt". It stores your steam filepath.  It will not include quotes, nor will you need to \ the spaces.  you can stop at the directory which includes Steam.exe.  For Windows, I do not believe you need to run as admin.  I never did and it works fine.  This may be a problem if you are a guest?  I can test more in the future.

###How to use it:

Simply make sure that it knows where your steam is installed, then start your steam download(s).  It does not matter how many games you download.  Then run the program and go to bed / to the gym / wherever you want to go, and this will sleep/shutdown your computer once everything is done downloading.

##_

Also, there is a python file named debug test.  There was a very weird bug I encountered and it took too long to fix so I cut functionality so that I won't have to work on this for more than one day.  But one day I will come back to fix it.  That python script reproduces the error.

##_
I literally give no cruds what anyone does with this so I am not going to even bother attaching my own license to it.  But I will put this on the end to save myself:

THIS SOFTWARE COMES WITH NO WARRANTY AND I AM NOT RESPONSIBLE FOR ANY DAMAGES CAUSED BY IT IN ANY CAPACITY.
