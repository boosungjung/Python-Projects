import pyautogui as py
import time, sys

delay = 0.05

class Click():

    def __init__(self):
        self.delay = delay
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def run(self):
        while self.program_running:
            while self.running:
                py.click()
                time.sleep(self.delay)


input = Click

def on_press(key):
    if key == py.keyDown('r'):
        input.start_clicking()


