import win32gui
import os
import multiprocessing
import time
def wallpaper():
    hProgman = win32gui.FindWindow("Progman", None)
    print(hProgman)
    win32gui.SendMessageTimeout(hProgman, 0x52c, 0, 0, 0, 0)
    hWorkerW = 0
    nW = 0
    x = 0
    y = 0
    def demo (hwnd, lparam):
        hD = win32gui.FindWindowEx(hwnd, hWorkerW, "SHELLDLL_DefView", None)
        if (hD != 0):
            global x
            x = hD
            nW = win32gui.FindWindowEx(0,hwnd,"WorkerW",None)
            if (nW != 0):
                global y
                y = nW
    win32gui.EnumWindows(demo, 0)
    video = win32gui.FindWindow(None,"c:/Users/huang/Downloads/1.mp4")
    win32gui.ShowWindow(y,0)
    print(video, hProgman)
    win32gui.SetParent(video, hProgman)
#def video():
#    os.system("C:\\Users\\huang\\Downloads\\video_studio\\ffmpeng\\bin\\ffplay.exe c:\\Users\\huang\\Desktop\\video.mp4")
#if __name__ == '__main__':
#    v = multiprocessing.Process(target=video, args=[])
#    w = multiprocessing.Process(target=wallpaper, args=[])
#    v.start()
#    time.sleep(0.5)
#    w.start()
wallpaper()

