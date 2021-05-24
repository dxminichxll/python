import pyautogui
import time

time.sleep(5)

while True:
    pyautogui.typewrite('french is fun')
    time.sleep(1)
    pyautogui.press('enter')
    # time.sleep(1)
    pyautogui.typewrite('french is easy')
    time.sleep(1)
    pyautogui.press('enter')
    # time.sleep(1)
    pyautogui.typewrite('french is fun AND easy')
    time.sleep(1)
    pyautogui.press('enter')
