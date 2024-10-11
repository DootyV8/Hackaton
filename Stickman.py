from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

while True:
    try:
        # Try to locate the image on screen
        stickman_location = pyautogui.locateOnScreen('stickman.png')

        if stickman_location is not None:
            print("I can see")
        else:
            print("I cannot see")

    except pyautogui.ImageNotFoundException:
        print("I cannot see")

    time.sleep(0.5)