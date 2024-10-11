import pyautogui
import time
from PIL import ImageGrab

try:
    while True:
        # Get the current mouse position
        x, y = pyautogui.position()

        # Capture the screen and get the pixel color at the mouse position
        screen = ImageGrab.grab()
        color = screen.getpixel((x, y))

        # Print the mouse position and the color
        print(f"X: {x}, Y: {y}, Color: {color}")  # "\r" to overwrite the previous line
        time.sleep(0.1)  # Add a delay to reduce CPU usage
except KeyboardInterrupt:
    print("\nProgram terminated.")