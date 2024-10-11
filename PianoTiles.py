from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Tile 1 Position: X: -1579 Y: 1130 RGB: (30,31,34)
#Tile 2 Position: X: -1372 Y: 1130 RGB: (30,31,34)
#Tile 3 Position: X: -1169 Y: 1130 RGB: (30,31,34)
#Tile 4 Position: X: -985 Y: 1130 RGB: (30,31,34)
#https://www.agame.com/game/magic-piano-tiles

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(-1579,1130) [0] == 0: #[0] is for R value from rgb [1] for r etc
        click(-1579,1130)
    if pyautogui.pixel(-1372,1130) [0] == 0:
        click(-1372,1130)
    if pyautogui.pixel(-1169,1130) [0] == 0:
        click(-1169,1130)
    if pyautogui.pixel(-985,1130) [0] == 0:
        click(-985,1130)