import sys
from math import factorial
from decimal import Decimal, getcontext
import keyboard
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

figure = plt.figure(figsize=(12,6))
getcontext().prec=1000

# Chudnovsky algorithm for figuring out pi
#Cal function was obtained from stackoverflow, it was written by user named Deepak Keshari
#https://stackoverflow.com/a/56456680
def cal(n):
    t = Decimal(0)
    pi = Decimal(0)
    deno = Decimal(0)

    for k in range(n):
        t = ((-1)**k)*(factorial(6*k))*(13591409+545140134*k)
        deno = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
        pi += Decimal(t)/Decimal(deno)
    pi = pi * Decimal(12) / Decimal(640320 ** Decimal(1.5))
    pi = 1/pi
    return round(pi,n)

def currNum(piNum):
    strPi = str(piNum)
    strPi = strPi[len(strPi) - 1]
    return int(strPi)

def plot(numDict):
    numbers = [0,1,2,3,4,5,6,7,8,9]
    slices = []
    for i in range(10):
        slices.append(numDict[i])

    colors = ['tab:blue','tab:orange','tab:green','tab:red','tab:purple','tab:brown','tab:pink','tab:gray','tab:olive','tab:cyan']

    plt.cla()#To clear the previous drawing so you can draw the updated chart

    plt.pie(slices, labels=numbers, colors=colors,
            startangle=90, explode = (0.1, 0.1, 0.1, 0.1,0.1,0.1,0.1,0.1,0.1,0.1),
            radius=1.0, autopct='%1.1f%%')



digitDict = dict()

for i in range(0,10):
    digitDict[i] = 0
    if i == 3:
        digitDict[i] += 1

run = True
nth = 1

while run:
    if keyboard.is_pressed("q"):#Press and hold q to terminate program
        sys.exit()

    digitDict[currNum(cal(nth))] += 1
    nth += 1

    ani = FuncAnimation(figure, plot(digitDict), interval=1000)
    plt.pause(0.9)
    plt.draw()





