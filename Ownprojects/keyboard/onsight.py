import pyautogui
import time
from pynput.mouse import Button, Controller

mouse = Controller()

print(pyautogui.size())

while True:
    pyautogui.moveTo(500, 520, duration=0.5)
    pyautogui.click(button='right')
    pyautogui.moveTo(550, 760, duration=0.5)
    pyautogui.moveTo(770, 760, duration=0.5)
    pyautogui.moveTo(770, 75, duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(870, 550, duration=0.5)
    pyautogui.click()
    time.sleep(1)
    mouse.scroll(0, 2)
    # time.sleep(1)




# pyautogui.moveTo(500, 520, duration=1)
# pyautogui.click(button='right')
# pyautogui.moveTo(550, 760, duration=1)
# pyautogui.moveTo(770, 760, duration=1)
# pyautogui.moveTo(770, 75, duration=1)
# pyautogui.click()
