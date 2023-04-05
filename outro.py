#outro stuff
import vlc #pip install python-vlc
import time
import os
from ctypes import windll
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_ulong
from ctypes import POINTER
from ctypes import byref

crash = False #Set to True if you want to BSOD

nullptr = POINTER(c_int)()
windll.ntdll.RtlAdjustPrivilege(
    c_uint(19), 
    c_uint(1), 
    c_uint(0), 
    byref(c_int())
)

file_to_play = (r'./Outro.wav')

OutroFile = vlc.MediaPlayer(file_to_play) 
OutroFile.play()

TimeInSeconds = 10

while TimeInSeconds > 0:
    timetoprint =("shutting down in: {}").format(TimeInSeconds)
    print(timetoprint)
    TimeInSeconds-=1
    time.sleep(1)

OutroFile.stop()
if crash == True:
    windll.ntdll.NtRaiseHardError(
        c_ulong(0xC000007B), 
        c_ulong(0), 
        nullptr, 
        nullptr, 
        c_uint(6), 
        byref(c_uint())
    )
else:
    os.system('shutdown /s /t 0')