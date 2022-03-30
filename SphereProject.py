from vpython import *
import random
import math

def sphereShape(size):
    rad = size

    sph = sphere(pos=vector(0, 0, 0), radius=rad, color=color.yellow, opacity=0.3)


def makeGrid(maxX, intervals):
    # y-axis
    curve(pos=[vector(0, maxX, 0), vector(0, -maxX, 0)], color=color.blue)
    # x-axis
    curve(pos=[vector(maxX, 0, 0), vector(-maxX, 0, 0)])
    # z-axis
    curve(pos=[vector(0, 0, maxX), vector(0, 0, -maxX)])
    num = -maxX
    for y in range(-maxX, maxX + intervals, intervals):
        text(pos=vector(2,y,0),text=str(num),billboard=True)
        curve(pos=[vector(1, y, 0), vector(-1, y, 0)])
        num+=intervals
    for x in range(-maxX, maxX + intervals, intervals):
        curve(pos=[vector(x, 1, 0), vector(x, -1, 0)])
    for z in range(-maxX, maxX + intervals, intervals):
        curve(pos=[vector(0, 1, z), vector(0, -1, z)])


def distanceForm(x, y, z, radi):
    square = sqrt(((x) ** 2 + (y) ** 2 + z ** 2))
    if square > radi:
        return square

    return round(square)

def plotPoints(rad,pointss):
    pointCount = 0
    listPoints = list()
    while pointCount <= pointss:
        dotX = random.randint(-rad, rad)
        dotY = random.randint(-rad, rad)
        dotZ = random.randint(-rad, rad)

        if vector(dotX,dotY,dotZ) in listPoints:
            continue
        else:
            if distanceForm(dotX,dotY,dotZ,rad) == rad:
                listPoints.append(vector(dotX,dotY,dotZ))
                pointCount += 1
    return listPoints

radius = 20

sphereShape(radius)
makeGrid(50, 5)
plotList = plotPoints(radius,50)
points(pos=plotList, radius=4, color=color.red)
# TODO
#    Find a way to label every tick on grid.Find a way to replicate the vector from Adam's file.Think of another creative idea to add.
