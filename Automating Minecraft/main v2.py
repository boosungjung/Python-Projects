from pymouse import PyMouseEvent
from threading import Thread


def __init__(self):
    PyMouseEvent.__init__(self)


def print_message(self):
    while self.do == 1:
        print("click")


class DetectMouseClick(PyMouseEvent):
    def click(self, x, y, button, press):
        if button == 1:
            if press:
                print("click")
                self.do = 1
                self.thread = Thread(target = self.print_message)
                self.thread.start()
            else:
                self.do = 0
                print("end")
        else:
            self.do = 0
            self.stop()

O = DetectMouseClick()
O.run()