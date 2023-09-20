import win32gui
import os
pid = 0
os.system('tasklist | findstr ffplay > C:\\Users\\huang\\Desktop\\cache.txt')
x = open("C:\\Users\\huang\\Desktop\\cache.txt","r").read()
for i in range(29,34):
    pid = str(pid) + str(x[i])
pid = pid[1:]
os.system(f'taskkill /f /PID {pid}')
os.system('del C:\\Users\\huang\\Desktop\\cache.txt')    


