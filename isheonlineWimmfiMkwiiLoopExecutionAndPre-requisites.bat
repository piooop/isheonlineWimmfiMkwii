@echo off
IF NOT EXIST C:\Python27 (
         wget.exe https://www.python.org/ftp/python/2.7.18/python-2.7.18.amd64.msi
         .\python-2.7.18.amd64.msi
         del .\python-2.7.18.amd64.msi
)
IF EXIST .\apseo.py (
     IF EXIST C:\Python27\apseo.py (
          del C:\Python27\Lib\apseo.py
     )
     IF EXIST C:\Python27\apseo.pyc (
          del C:\Python27\Lib\apseo.pyc
     )
     copy .\apseo.py C:\Python27\Lib\
     del .\apseo.py
)
REM comment_out: This copies the file apseo.py to python library folder if in folder
IF NOT EXIST C:\Python27\p.mp3 (
         wget https://vgmsite.com/soundtracks/mario-kart-wii/yenpskzutw/3-32%20Finish%20OK%20%26%20Winning%20Results%20%28Race%29.mp3           
         copy .\p.mp3 C:\Python27
         del .\p.mp3
         copy 3-32 Finish OK & Winning Results (Race).mp3 p.mp3
         del 3-32 Finish OK & Winning Results (Race).mp3
)
REM comment_out: If you don't have the music file it downloads it and copies it to python folder and deletes the one downloaded
C:\Python27\Scripts\pip.exe install wget
REM comment_out: Installs or updates wget
C:\Python27\Scripts\pip.exe install python-vlc
REM comment_out: Installs or updates python-vlc
C:\Python27\python.exe Loop.py
REM comment_out: Runs loop script

