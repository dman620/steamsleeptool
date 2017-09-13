## HELLO THIS IS MY README

Version 1.0

Windows 10, Python3 used

### What is it:

It is a Python script, which will sleep or shutdown your computer whenever your steam games are finished downloading. You can change that in the config file.

### How it works:

This program takes advantage of Steam's "downloading" folder, which stores temporary files in it while a download is happening. It simply monitors this folder and sleeps/shuts down your computer once it is empty (i.e. once the download is finished).

### Why should you use:

Of course automation is better! You can activate this script and go to the pool, and you can rest assured that you will not waste any electricity, or wear on your computer! Of course the difference is probably minimal, but it always bothered me that I had to leave my computer on for the whole night just to download one 9GB game.

### Tested for:

This is currently only built on Windows. Tested on Windows 10 and made with Python3. Though it should work for any Windows version for which the commands I use are still functional, and obviously for which Steam is still compatible. It is such a short program that you can easily adapt it for other operating systems or versions.

### Setup:

This comes with a "config.txt". It stores your Steam filepath. It will not include quotes, nor will you need to \ the spaces. You can stop at the directory which includes Steam.exe.

For Windows, I do not believe you need to run as admin. I never did and it works fine. This may be a problem if you are a guest.

### How to use it:

Simply make sure that it knows where your Steam is installed, then start your Steam download(s). It does not matter how many games you download. Then run the program and go to bed/to the gym/wherever you want to go, and this will sleep/shutdown your computer once everything is done downloading.

## _

Also, there is a Python file named debug test. There was a very weird bug I encountered and it took too long to fix so I cut functionality so that I won't have to work on this for more than one day. But eventually I will come back to fix it. That Python script reproduces the error.

