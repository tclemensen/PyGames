import sys
import os
if (sys.platform == "win32"):
    import winsound
if (sys.platform == "linux"):
    from playsound import playsound


def playSFX():
    if (sys.platform == "linux"):
        #os.system("aplay pong.wav&")
        playsound("/home/trond/Documents/repos/PyGames/pong.wav")        
    elif (sys.platform == "win32"):
        winsound.PlaySound("pong.wav", winsound.SND_ASYNC)
    elif (sys.platform == "darwin"):
        os.system("afplay pong.wav&")
