import os
import platform
import subprocess
from shutil import which

#Checking whether Spotify exists on the operating system
#Need this so I can throw an exception if it doesn't exist
def program_checker(name):
    if which(name) is not None:
        return True
    return False

print(program_checker("spotify"))
print(which("spotify"))

#Check to see if other apps have audio
#Need this to check when to stop Spotify

#Logic to stop Spotfiy if another app is playing audio

#Logic to resume Spotify when audio stops playing

