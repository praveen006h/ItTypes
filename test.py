import time
import win32con
import win32api
from win32api import keybd_event, mouse_event, GetKeyState


keys = {'\t': 0x09,
        '\n': 0x0D,
        ' ': 0x20,
        'a': 0x41,
        'b': 0x42,
        'c': 0x43,
        'd': 0x44,
        'e': 0x45,
        'f': 0x46,
        'g': 0x47,
        'h': 0x48,
        'i': 0x49,
        'j': 0x4A,
        'k': 0x4B,
        'l': 0x4C,
        'm': 0x4D,
        'n': 0x4E,
        'o': 0x4F,
        'p': 0x50,
        'q': 0x51,
        'r': 0x52,
        's': 0x53,
        't': 0x54,
        'u': 0x55,
        'v': 0x56,
        'w': 0x57,
        'x': 0x58,
        'y': 0x59,
        'z': 0x5A,
        ';': 0xBA,
        '[': 0xDB,
        '\\': 0xDD,
        ']': 0xDD,
        }

time.sleep(3)

a = "f\nasdsasd;"
A = a.lower()
for i in A[:-1]:
    keybd_event(keys[i], 0, 1, 0)
    print(i+"   ",GetKeyState(keys[i]))
    keybd_event(keys[i], 0, 2, 0)
    print(i+"   ",GetKeyState(keys[i]))




time.sleep(1)
