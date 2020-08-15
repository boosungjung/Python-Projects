import pyautogui as py
import time, sys

time.sleep(2)
distance = 200
try:
    while distance > 0:
        py.dragRel(-distance, 0, duration = 5)
        distance -= 50
except KeyboardInterrupt:
    sys.exit()