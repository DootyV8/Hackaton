from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# Try to locate the 'stickman.png' image with a confidence level
stickman_location = pyautogui.locateOnScreen('stickman.png', confidence=0.8)
print(stickman_location)
