from tkinter import *
from tkinter.ttk import *
from collections import deque

# for i in range(100):
#     print(i , '\033[' + str(i) + 'm' + 'Test' + '\033[0m')


x = deque([1,2,3,4])
x.rotate(-1)
print(x)