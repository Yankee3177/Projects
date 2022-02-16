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

def inShape(inShapeSize,x,y,z,shapeNum):
    if shapeNum == 3:
        if abs(x) <= int(inShapeSize[0]/2)and abs(y) <= int(inShapeSize[0]/2) and abs(z) <= int(inShapeSize[0]/2):
            return True
        return False

    if shapeNum == 2:
        if abs(x) <= int(inShapeSize[0]/2) and abs(y) <= int(inShapeSize[1]/2) and abs(z) <= int(inShapeSize[2]/2):
            return True
        return False

    if (x ** 2 + y**2 + z**2) < inShapeSize[0]:
        return True
    return False


def plotPoints(shapeNum,outSize,inSize,inShapeNum):
    counter = 0
    listPoints = list()
    newList = outSize.copy()

    if shapeNum == 1 or shapeNum == 3:
        for i in range(100):
            dotX = random.randint(-int(newList[0] / 2), int(newList[0] / 2))
            dotY = random.randint(-int(newList[0] / 2), int(newList[0] / 2))
            dotZ = random.randint(-int(newList[0] / 2), int(newList[0] / 2))
            listPoints.append(vector(dotX,dotY,dotZ))

            if inShape(inSize,dotX,dotY,dotZ,inShapeNum):
                counter+=1

    else:
        for j in range(100):
            recX = random.randint(-int(newList[0]/2),int(newList[0]/2))
            recY = random.randint(-int(newList[1]/2),int(newList[1]/2))
            recZ = random.randint(-int(newList[2]/2),int(newList[2]/2))
            listPoints.append(vector(recX, recY, recZ))

            if inShape(inSize,recX,recY,recZ,inShapeNum):
                counter+=1

    return listPoints,counter



outShape = True
shapes = list()
outShapeSize = list()
inShapeSize = list()
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

plotList,pointIn = plotPoints(shapes[0],outShapeSize,inShapeSize,shapes[1])
points(pos=plotList, radius=5, color=color.red)

print("This is how many points touched the inside shape: ", pointIn)