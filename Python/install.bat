set PATH=%PATH%;C:\Program Files\7-Zip
cd /d %USERPROFILE%
bitsadmin /transfer winpython https://github.com/naka-tomo/image_proc_exp/blob/master/Python/WinPython.zip?raw=true %CD%\winpython.zip
7z x -y winpython.zip
cd /d %~dp0
echo "%USERPROFILE%\WinPython\IDLEX (Python GUI).exe" > winpython.bat
pause
