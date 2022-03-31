import time
from vpython import *
import random
import math


def sphereShape(size):
    rad = size

    sphere(pos=vector(0, 0, 0), radius=rad, color=color.yellow, opacity=0.3)


def makeGrid(maxX, intervals):
    # y-axis
    curve(pos=[vector(0, maxX, 0), vector(0, -maxX, 0)], color=color.blue)
    # x-axis
    curve(pos=[vector(maxX, 0, 0), vector(-maxX, 0, 0)], color=color.green)
    # z-axis
    curve(pos=[vector(0, 0, maxX), vector(0, 0, -maxX)], color=color.red)
    num = -maxX

    for y in range(-maxX, maxX + intervals, intervals):
        text(pos=vector(2, y, 0), text=str(num), billboard=True)
        curve(pos=[vector(1, y, 0), vector(-1, y, 0)], color=color.white)
        num += intervals
    num = -maxX
    for x in range(-maxX, maxX + intervals, intervals):
        text(pos=vector(x, 2, 0), text=str(num), billboard=True)
        curve(pos=[vector(x, 1, 0), vector(x, -1, 0)], color=color.white)
        num += intervals
    num = -maxX
    for z in range(-maxX, maxX + intervals, intervals):
        text(pos=vector(0, 2, z), text=str(num), billboard=True)
        curve(pos=[vector(0, 1, z), vector(0, -1, z)], color=color.white)
        num += intervals


def distanceForm(x, y, z, radi):
    square = sqrt((x ** 2 + y ** 2 + z ** 2))
    if square > radi:
        return square
    if square < (radi - 0.5):
        return square

    return round(square)


def plotPoints(rad, pointss):
    pointCount = 0
    listPoints = list()

    while pointCount < pointss:
        if pointss == 0:
            return listPoints
        dotX = random.randint(-rad, rad)
        dotY = random.randint(-rad, rad)
        dotZ = random.randint(-rad, rad)

        dotPos = vector(dotX, dotY, dotZ)

        if dotPos in listPoints:
            continue
        else:
            if distanceForm(dotX, dotY, dotZ, rad) == rad:
                listPoints.append(dotPos)
                pointCount += 1

    return listPoints

radius = int(input("Enter a whole number greater than 5 for the radius: "))
while radius < 5:
    radius = int(input("Try again, Enter a whole number greater than 5: "))

pointsPlot = int(input("How many points do you want to plot? "))
while pointsPlot < 0:
    pointsPlot = int(input("Enter a positive number...  "))

sphereShape(radius)
makeGrid(radius*3, 5)
plotList = plotPoints(radius, pointsPlot)
points(pos=plotList, radius=4, color=color.red)

for vec in plotList:
    line = curve(pos=[vector(0, 0, 0),vec],color=color.cyan,visible=True)
    time.sleep(1)
    line.visible = False
