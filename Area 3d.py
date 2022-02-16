from vpython import *
import random
import math

def rectangularCuboid(size):
    x = size[0]
    y = size[1]
    z = size[2]

    boxx = box(pos=vector(0, 0, 0), length=x, height=y, width=z, opacity=0.5)

    volume = x * y * z
    print("The volume of the rectangular cube is: ", volume)


def cube(size):
    ele = size[0]
    boxx = box(pos=vector(0, 0, 0), length=ele, height=ele, width=ele, opacity=0.5)

    volume = ele**3
    print("The volume of the cube is: ", volume)

def sphereShape(size):
    rad = size[0]

    sph = sphere(pos=vector(0, 0, 0), radius=rad, color=color.yellow, opacity=0.5)

    volume = round((4/3)*math.pi*(rad**3),4)
    print("The volume of the sphere is: ", volume)

def drawShape(shapeNumber,size,outShape):
    shapeSize = size.copy()
    if shapeNumber == 1:  # sphere
        if not outShape:
            shapeSize[0] = shapeSize[0]/2
        sphereShape(shapeSize)
    elif shapeNumber == 2:  # rectangular cube
       rectangularCuboid(shapeSize)
    else:#cube
        cube(shapeSize)

def outSize(shapeNum):
    sizeList = list()
    if shapeNum == 1 or shapeNum == 3:
        sizeList.append(random.randint(40,70))
    else:
        sizeList.append(random.randint(40,70))
        sizeList.append(random.randint(30,60))
        while sizeList[1] > sizeList[0]:
            sizeList[1] = random.randint(30,60)
        sizeList.append(sizeList[1])
    return sizeList

def inSize(shapeNum):
    sizeList = list()
    if shapeNum == 1 or shapeNum == 3:
        sizeList.append(random.randint(15, 25))
    else:
        sizeList.append(random.randint(15, 25))
        sizeList.append(random.randint(5, 24))

        while sizeList[1] > sizeList[0]:
            sizeList[1] = random.randint(5, 24)

        sizeList.append(sizeList[1])
    return sizeList

def plotPoints(shapeNum,outSize):
    listPoints = list()
    newList = outSize.copy()

    if shapeNum == 1 or shapeNum == 3:
        for i in range(100):
            dotX = random.randint(-int(newList[0] / 2), int(newList[0] / 2))
            dotY = random.randint(-int(newList[0] / 2), int(newList[0] / 2))
            dotZ = random.randint(-int(newList[0] / 2), int(newList[0] / 2))
            listPoints.append(vector(dotX,dotY,dotZ))
    else:
        for j in range(100):
            recX = random.randint(-int(newList[0]/2),int(newList[0]/2))
            recY = random.randint(-int(newList[1]/2),int(newList[1]/2))
            recZ = random.randint(-int(newList[2]/2),int(newList[2]/2))
            listPoints.append(vector(recX, recY, recZ))
    return listPoints



outShape = True
shapes = list()
outShapeSize = 0
inShapeSize = 0
for i in range(2):
    shape = random.randint(1,3) #This grabs a random index number
    shapes.append(shape)
    if outShape:
        outShapeSize = outSize(shape)
        drawShape(shape,outShapeSize,outShape)
        outShape = False
    else:
        inShapeSize = inSize(shape)
        drawShape(shape,inShapeSize,outShape)

listt = plotPoints(shapes[0],outShapeSize)
points(pos=listt, radius=5, color=color.red)