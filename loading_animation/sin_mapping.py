import math
import matplotlib.pyplot as plt
import numpy as np

pi = math.pi

x = np.arange(0 , 2 * pi , 0.1)
y = np.sin(x)
plt.plot(x , y)




def rounder(num):
    if num > 0.7:
        return 1
    if 0 < num <= 0.7:
        return 0.5
    if -0.7 < num <= 0:
        return -0.5
    if num <= -0.7:
        return -1

def rounder2(num):
    if num > 0.7:
        return 1
    if 0.3 < num <= 0.7:
        return 0.5
    if -0.3 < num <= 0.3:
        return 0
    if -0.7 < num <= -0.3:
        return -0.5
    if num <= -0.7:
        return -1

length = 30
d = [x for x in range(length)]
denum = 5
angle = [pi / (denum +1) + x * pi / denum for x in d]
print(math.sin(pi / (denum * length)))
# print(angle)
for i in range(1):
    pos = [math.sin(rad) for rad in angle]
    plt.scatter(range(len(pos)) , pos)
    print(pos)
    for j in range(len(pos)):
        pos[j] = rounder2(pos[j])
    plt.scatter(range(len(pos)) , pos)
    print(pos)
    angle = [rad + pi / denum for rad in angle]
    print('*' * 50)



half = [0.7 for i in range(length)]
half2 = [-0.7 for i in range(length)]
zero = [0.3 for i in range(length)]
zero2 = [-0.3 for i in range(length)]

plt.plot(half , color='black' , linestyle='--')
plt.plot(half2 , color='black' , linestyle='--')
plt.plot(zero , color='black' , linestyle='--')
plt.plot(zero2 , color='black' , linestyle='--')

plt.show()
