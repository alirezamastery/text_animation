import struct
import timeit
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pandas as pd
import numpy as np
import sys
import os
import math
import time
import pandas as pd
import datetime as dt
import random
import time
import ctypes

# import tornado

kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

HIDE_CURSOR = '\x1b[?25l'
sys.stdout.write('\x1b[?25l')

# while True:
#     pos = random.randint(0 , 173)
#     length = random.randint(5 , 20)
#     for l in range(length):
#         for col in range(172):
#             if col == pos:
#                 sys.stdout.write('│')
#             else:
#                 sys.stdout.write(' ')
#         sys.stdout.write('\n' + HIDE_CURSOR)
#         time.sleep(0.02)

while True:
    num = random.randint(1, 5)
    pos = []
    # length = []
    for i in range(num):
        pos.append(random.randint(0, 173))
    length = random.randint(5, 20)

    for col in range(172):
        if col in pos:
            sys.stdout.write('│')
        else:
            sys.stdout.write(' ')
    sys.stdout.write('\n' + HIDE_CURSOR)
    time.sleep(0.02)
