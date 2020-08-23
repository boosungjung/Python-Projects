from pynput.mouse import Button, Controller
from pynput import mouse
import time

cps = 15
delay = 1/cps


def on_hold():
    mouse = Controller()
    mouse.click(Button.left)
    time.sleep(delay)

while True:
    with mouse.Listener(on_hold=on_hold) as listener:
        listener.join()
