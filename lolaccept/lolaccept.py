import pyautogui
import time
import os
import sys

def_path = os.path.dirname(os.path.abspath(sys.argv[0]))--

def queue():
    while 1:
        global def_path
        accbutt = pyautogui.locateOnScreen(def_path+r'\pictures\accept\lolaccept.png', grayscale=True, confidence=.8)
        time.sleep(3)
        if accbutt is not None:
            pyautogui.click(accbutt)
        pass

queue()
