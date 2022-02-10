import turtle as tur
import math
import random

tur.screensize(canvwidth=2000, canvheight=2000)
tur.speed(10)
tur.hideturtle()

areaList = []
def circle(size):
    tur.circle(size)
    area = round(math.pi * size ** 2,4)
    print("Area of circle is: ", area)
    areaList.append(area)
    return [(0.00,0.00)]

def square(size):
    startPos = tur.pos()
    for i in range(4):
        tur.forward(size)
        tur.left(90)
    tur.setheading(0)

    area = size ** 2
    print("Area of square is: ", area)
    areaList.append(area)
    return startPos


def rectangle(size):
    startPos = tur.pos()
    for i in range(2):
        tur.forward(size)
        tur.left(90)
        tur.forward(size/2)
        tur.left(90)
    base = size
    height = size/2

    area = base * height
    print("Area of the rectangle is: ", area)
    areaList.append(area)
    return startPos

def drawShape(shapeNumber,size):
    if shapeNumber == 1:  # Circle
        begPos = circle(size)
    elif shapeNumber == 2:  # Rectangle
       begPos = rectangle(size)
    else:#Square
        begPos = square(size)
    return begPos

def plotPoints(size,shapeNum,startPosX,xSecShape,inShape,inSize,ySecShape):
    counter = 0
    if shapeNum == 3:#Square
        start = startPosX
        for i in range(100):
            dotX = random.randint(start,size)
            dotY = random.randint(0,size)
            tur.penup()
            tur.goto(dotX,dotY)
            tur.pendown()
            tur.dot()
            if checkIn(inShape,xSecShape,ySecShape,inSize):
                counter+= 1

    elif shapeNum == 2:
        start = startPosX
        for i in range(100):
            xLim = start + size
            dotX = random.randint(start, xLim)
            dotY = random.randint(0, size//2)
            tur.penup()
            tur.goto(dotX, dotY)
            tur.pendown()
            tur.dot()
            if checkIn(inShape,xSecShape,ySecShape,inSize):
                counter+= 1
    else:
        tur.penup()
        tur.goto(0,0)
        tur.setheading(0)
        tur.left(90)
        tur.forward(size)
        tur.setheading(0)
        mid = tur.pos()
        for i in range(100):
            tur.penup()
            dotX = random.randint(-(size),size*2)
            dotY = random.randint(-(size),size*2)

            tur.goto(dotX,dotY)
            if tur.distance(mid) > size: #if it's past the radius then it's outside the circle
                continue
            tur.pendown()
            tur.dot()
            if checkIn(inShape,xSecShape,ySecShape,inSize):
                counter+= 1
    return counter


def checkIn(shape,xCorr,yCorr,size):

    xCor = xCorr
    yCor = yCorr
    if shape == 3:
        if tur.xcor() >= xCor and tur.xcor() <= (xCor + size) and tur.ycor() >= yCor and tur.ycor() <= (yCor + size):
            return True
        return False
    elif shape == 2:
        if tur.xcor() >= xCor and tur.xcor() <= (xCor + size) and tur.ycor() >= yCor and tur.ycor() <= (yCor + (size//2)):
            return True
        return False
    currPos = tur.pos()
    tur.goto(xCorr,yCorr)
    tur.setheading(0)
    tur.left(90)
    tur.forward(size)
    tur.setheading(0)
    insideMid = tur.pos()
    tur.goto(currPos)
    if tur.distance(insideMid) > size:
        return False
    return True



shapeList = [1,2,3]

outShapeSize = random.randint(300,400)
inShapeSize = random.randint(50,100)
outShape = True
outsideShape=[]
pos = list()

for i in range(2):
    shape = random.randint(1,3) #This grabs a random index number
    outsideShape.append(shape)
    if outShape:
        pos.append(drawShape(shape,outShapeSize))
        outShape = False
    else:
        if outsideShape[0] == 1:
            tur.setheading(0)
            tur.penup()
            tur.left(90)
            tur.forward(outShapeSize/2)
            tur.setheading(0)
            tur.pendown()
            tur.color("blue")
            if shape == 1 and outsideShape[0] > 1:
                pos.append(drawShape(shape,inShapeSize))
            else:
                pos.append(drawShape(shape, inShapeSize))

        elif outsideShape[0] == 2:
            tur.penup()
            tur.setheading(0)
            tur.forward(outShapeSize/2)
            tur.color("blue")
            tur.pendown()
            if shape == 1:
                pos.append(drawShape(shape, inShapeSize ))
            else:
                pos.append(drawShape(shape, inShapeSize))

        else:
            tur.setheading(0)
            tur.penup()
            tur.forward(inShapeSize)
            tur.color("blue")
            tur.pendown()
            if shape == 1:
                pos.append(drawShape(shape, inShapeSize))
            else:
                pos.append(drawShape(shape, inShapeSize))

print("This is pos: ",pos)
xPos = pos[0][0]
secPosX = pos[1][0]
secPosY = pos[1][1]

insideShape = outsideShape[1]
pointIn = plotPoints(outShapeSize,outsideShape[0],xPos,secPosX,insideShape,inShapeSize,secPosY)

print(pointIn)

print("Actual Ratio = ",round(areaList[1]/areaList[0],4))


tur.done()