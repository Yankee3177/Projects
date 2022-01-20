import turtle as tur
import random


def terminate():
    '''
    e terminates the program
    Terminates the program and closes the window.
    '''
    tur.bye()


def isInScreen(win, obTri):
    """
    Returns True if the next point is inside the parameters of the window.
    :param win(Turtle object): The canvas on which we are drawing the triangles.
    :param obTri(Turtle object): The current triangle object we are drawing
    :return: True or False
    """
    leftBound = win.window_width() // -6
    rightBound = win.window_width() // 6
    bottomBound = win.window_height() // -6
    topBound = win.window_height() // 6

    turtleX = obTri.xcor()
    turtleY = obTri.ycor()

    if turtleX < leftBound or turtleX > rightBound or turtleY < bottomBound or turtleY > topBound:
        return False

    return True


def direction(triObj):
    """
    :param triObj(Turtle Object): The current turtle object we're on.
    :return: The X and Y coordinates for the next turtle object.
    """
    angleChange = random.randint(20, 170)
    typeChange = random.randint(1, 3)
    moveDir = ()

    if typeChange == 1:
        triObj.forward(200)
        moveDir = triObj.pos()

    if typeChange == 2:
        triObj.left(angleChange)
        triObj.forward(200)
        moveDir = triObj.pos()
        triObj.right(angleChange)

    if typeChange == 3:
        triObj.right(angleChange)
        triObj.forward(200)
        moveDir = triObj.pos()
        triObj.left(angleChange)

    return moveDir


def rightTri(rTri, posStart):
    """

    :param rTri: Turtle object
    :param posStart: X and Y coordinates
    :return: X and Y coordinates for the next Turtle object
    """
    inScreen = False
    rTri.speed(10)
    rTri.penup()
    rTri.goto(posStart)
    rTri.pendown()

    # Dictionary is used to store the angle.
    myDict = dict()
    myDict[1] = rTri.pos()
    rTri.forward(70)
    rTri.left(135)

    myDict[2] = rTri.pos()
    rTri.forward(100)
    rTri.setheading(0)
    rTri.right(90)

    myDict[3] = rTri.pos()
    rTri.forward(71)
    rTri.penup()

    while not inScreen:
        inScreen = isInScreen(tur, rTri)
        myDict[4] = direction(rTri)
        if not inScreen:
            rTri.setx(0)
            rTri.sety(0)
    rTri.setheading(0)

    for i in range(1, 4):
        rTri.goto(myDict[i])
        rTri.pendown()
        if i == 1:
            rTri.left(45)
            rTri.forward(200)
        elif i == 2:
            rTri.left(112.5)
            rTri.forward(200)
        else:
            rTri.setheading(0)
            rTri.right(68.5)
            rTri.forward(200)

        rTri.penup()
    return myDict[4]


def eqTri(eTri, startPos, size):
    """

    :param eTri: Turtle object.
    :param startPos: X and Y coordinates
    :param size(int): Decides how big the triangle is going to be.
    :return: X and Y coordinates for the next Turtle object
    """
    eTri.speed(10)
    inScreen = False
    eTri.penup()
    eTri.goto(startPos)
    eTri.pendown()

    # Dictionary is used to store the angle to draw the line for the circumcenter.
    myDict = dict()
    for pos in range(1, 4):
        eTri.left(120)
        myDict[pos] = eTri.pos()
        eTri.forward(size)
    eTri.penup()

    # This while loop is to ensure that the triangle being drawn is inside parameters specified for the window.
    while not inScreen:
        inScreen = isInScreen(tur, eTri)
        myDict[4] = direction(eTri)
        if not inScreen:
            eTri.setx(0)
            eTri.sety(0)

    for i in range(3, 0, -1):
        eTri.penup()
        eTri.goto(myDict[i])
        eTri.pendown()

        if i == 2:
            eTri.right(120)
            eTri.forward(size * 2)
            eTri.penup()
            eTri.right(150)  ##add 30 to 120 to account for the left 30 degree change in the else statement
        else:
            eTri.left(30)
            eTri.forward(size * 2)
            eTri.penup()
    return myDict[4]


start = (0, 0)
for i in range(1, 100):

    # This is used to constantly look for the e to be typed on the keyboard to terminate the program.
    tur.listen()
    tur.onkey(terminate, "e")

    tri = tur.Turtle()  # Initiate a new turtle object
    tri.ht()  # Hide the pointer so when you draw you just see the lines.

    randd = random.randint(1, 2)  # These numbers are used to decide which type of triangle to use
    if randd == 1:
        start = rightTri(tri, start)
    else:
        size = random.randint(100, 200)
        start = eqTri(tri, start, size)
    if i % 10 == 0 and i > 1:  # clear the screen after every 10 triangles.
        tur.clearscreen()

tur.done()  # keeps the window open
