import pyautogui
import pydirectinput
import time

pyautogui.FAILSAFE = True

screenWidth, screenHeight = pyautogui.size()
# while True:
#     print(pyautogui.position())


def left_click(hold_time):
    start = time.time()
    while time.time() - start < hold_time:
        pyautogui.click()

# left_click(1000)

# pyautogui.mouseDown()
# while True:
#     pyautogui.mouseDown()
#     time.sleep(10)
#     pyautogui.mouseUp()
#     pydirectinput.move(0, -100, duration=0.5)
#     pyautogui.mouseDown()
#     time.sleep(10)
#     pyautogui.mouseUp()
#     pydirectinput.moveTo(0, 100, duration=0.5)

print(pyautogui.size())
time.sleep(5)

pydirectinput.moveTo(1, 0, duration=0.5)
