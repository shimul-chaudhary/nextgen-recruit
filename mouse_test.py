import pyautogui as auto
import time

def get_mouse_position():
    while True:
        x, y = auto.position()
        print(f"X: {x}, Y: {y}")
        time.sleep(1)

get_mouse_position()

