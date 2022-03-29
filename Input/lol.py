import pyautogui
import time
for i in range(17*8):
    pyautogui.click(1283,214)
    time.sleep(1)
    pyautogui.click(250+((i%17)*100),150+(i//17)*100,clicks=2)
    time.sleep(10)
    pyautogui.click(1446,217)
    time.sleep(1)