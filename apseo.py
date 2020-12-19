import mmap
import wget
import os
import vlc
import glob
import time
def isonlineonwiimmfimkwii(mii):
 fileList = glob.glob('./index*')
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
    if s.find(mii) != -1:
        online="1"
        print " "
        print "He is online. Join!"
        player= vlc.MediaPlayer("C:\Python27\p.mp3")        
        player.play()
        time.sleep(86)
        file.close()
        s.close()
        os.remove("index.html")
        exit()
 file.close()
 s.close()
 os.remove("index.html")
 print " "
