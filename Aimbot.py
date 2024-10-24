from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#Color of center: (255, 87, 34)

while keyboard.is_pressed('q') == False:
    flag = 0
    pic = pyautogui.screenshot(region=(890, 380, 1000, 600))

    width, height = pic.size

    for x in range(0, width, 5):
        for y in range(0, height, 5):

            r, g, b = pic.getpixel((x, y))

            if b == 34 and r == 255 and g == 87:
                flag = 1
                click(x+890, y+380)
                time.sleep(0.01)
                break

        if flag == 1:
            break
