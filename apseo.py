import mmap
import wget
import os
import vlc
import glob
from time import time, ctime
import time as she
fileList = glob.glob('./index*')
def isonlineonwiimmfimkwii(fc):
 for filePath in fileList:
    try:
        os.remove(filePath)
    except:
        print("Error while deleting file : ", filePath)
 url="https://wiimmfi.de/stats/mkw/index.html"
 wget.download(url)
 file=open('index.html')
 with file as f:
    s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    if s.find(fc) != -1:
        online="1"
        print " "
        print fc + " is online. Join!"
        player= vlc.MediaPlayer("C:\Python27\p.mp3")        
        player.play()
        she.sleep(86)
        file.close()
        s.close()
        os.system('copy index.html "' + fc + 'Connection.html"')
        os.remove("index.html")
        t = time()
        f= open('./SomeoneConnected.txt', 'w+')
        f.write(fc + ' connected at ' + str(ctime(t)))
        f.close()
        exit()
 file.close()
 s.close()
 os.remove("index.html")
 print " "
