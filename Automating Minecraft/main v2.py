from pynput import mouse
from pynput.mouse import Button, Controller



def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False

# Collect events until released
while True:
    with mouse.Listener(
            on_click=on_click) as listener:
        listener.join()

