# plugined_bot.py
from ctypes import CDLL, c_float
import os

# IMPORTANT: absolute path avoids Windows DLL stupidity
BASE_DIR = os.path.dirname(__file__)
dll_path = os.path.join(BASE_DIR, "math_plugin.dll")

library = CDLL(dll_path)

library.add.argtypes = (c_float, c_float)
library.add.restype = c_float

library.sub.argtypes = (c_float, c_float)
library.sub.restype = c_float

library.mul.argtypes = (c_float, c_float)
library.mul.restype = c_float

library.divi.argtypes = (c_float, c_float)
library.divi.restype = c_float


# TEST (THIS PROVES IT WORKS)
print("TEST BEFORE BOT STARTS.")
print("add:", library.add(10.47, 6.29))
print("sub:", library.sub(10.2, 8.55))
print("mul:", library.mul(11.928, 9.226))
print("div:", library.divi(10.5, 8.9))
