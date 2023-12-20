@echo off
python -m pip install requests PyQt5 tqdm
echo msgbox "The packages have been downloaded." > %temp%\tempmessage.vbs
call %temp%\tempmessage.vbs
del %temp%\tempmessage.vbs
pause
