set WshShell = WScript.CreateObject("WScript.shell")
WshShell.Run("notepad.exe")
WScript.sleep 1000
WshShell.sendkeys "huang"
WshShell.sendkeys "jian"
WshShell.sendkeys 1

rem play = WScript.CreateObject("wmplayer.ocx")
rem Set server = GetObject("winmgmts:\\.\root\cimv2")
