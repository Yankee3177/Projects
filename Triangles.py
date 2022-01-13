import turtle as tur
import random


def isInScreen(win, james):
    leftBound = win.window_width() // -6
    rightBound = win.window_width() / 6
    bottomBound = win.window_height() // -6
    topBound = win.window_height() // 6

    turtleX = james.xcor()
    turtleY = james.ycor()

    if turtleX < leftBound or turtleX > rightBound or turtleY < bottomBound or turtleY > topBound:
        return False

    return True


def direction(james):
    angleChange = random.randint(20, 170)
    typeChange = random.randint(1, 3)
    moveDir = ()
    if typeChange == 1:
        james.forward(200)
        moveDir = james.pos()
    if typeChange == 2:
        james.left(angleChange)
        james.forward(200)
        moveDir = james.pos()
        james.right(angleChange)
    if typeChange == 3:
        james.right(angleChange)
        james.forward(200)
        moveDir = james.pos()
        james.left(angleChange)

    return moveDir


def rightTri(james, posStart):
    inScreen = False
    james.speed(10)
    james.penup()
    james.goto(posStart)
    james.pendown()

    myDict = dict()
    myDict[1] = james.pos()
    james.forward(70)
    james.left(135)
    myDict[2] = james.pos()
    james.forward(100)
    james.setheading(0)
    james.right(90)
    myDict[3] = james.pos()
    james.forward(71)
    james.penup()
    while not inScreen:
        inScreen = isInScreen(tur, james)
        myDict[4] = direction(james)
        if inScreen == False:
            james.setx(0)
            james.sety(0)
    james.setheading(0)

    for i in range(1, 4):
        james.goto(myDict[i])
        james.pendown()
        if i == 1:
            james.left(45)
            james.forward(200)
        elif i == 2:
            james.left(112.5)
            james.forward(200)
        else:
            james.setheading(0)
            james.right(68.5)
            james.forward(200)

        james.penup()
    return myDict[4]


def eqTri(james, startPos, size):
    james.speed(10)
    inScreen = False
    james.penup()
    james.goto(startPos)
    james.pendown()

    myDict = dict()
    for i in range(1, 4):
        james.left(120)
        myDict[i] = james.pos()
        james.forward(size)
    james.penup()
    while not inScreen:
        inScreen = isInScreen(tur, james)
        myDict[4] = direction(james)
        if not inScreen:
            james.setx(0)
            james.sety(0)

    for i in range(3, 0, -1):
        james.penup()
        james.goto(myDict[i])
        james.pendown()
        if i == 2:
            james.right(120)
            james.forward(size * 2)
            james.penup()
            james.right(150)  ##add 30 to 120 to account for the left 30 degree change in the else statement
        else:
            james.left(30)
            james.forward(size * 2)
            james.penup()
    return myDict[4]


start = (0, 0)
for i in range(1, 100):
    james = tur.Turtle()
    james.ht()
    randd = random.randint(1, 2)
    if randd == 1:
        start = rightTri(james, start)
    else:
        size = random.randint(100, 200)
        start = eqTri(james, start, size)
    if i % 10 == 0 and i > 1:
        tur.clearscreen()

tur.done()
