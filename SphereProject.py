from vpython import *


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

    for y in range(-maxX, maxX + intervals, intervals):
        curve(pos=[vector(1, y, 0), vector(-1, y, 0)])
    for x in range(-maxX, maxX + intervals, intervals):
        curve(pos=[vector(x, 1, 0), vector(x, -1, 0)])
    for z in range(-maxX, maxX + intervals, intervals):
        curve(pos=[vector(0, 1, z), vector(0, -1, z)])


sphereShape(20)
makeGrid(50, 2)
