--- xxx.bat ---

@echo off
set DEV= (sys.argv[1])
set OBJ= (sys.argv[2])
py -u "CheckFile.py" %DEV% %OBJ%
echo %ERRORLEVEL%
pause
--- yyy.py ---