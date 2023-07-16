import turtle as tur
import random as rnd


def readFile():
    with open("EulersNum.txt", "r") as f:
        data = f.read()
        data.strip(" ")
        data = data.replace(".", "")
        data = data.replace(" ", "")

        return data


def terminateProg():
    tur.listen()
    tur.onkey(tur.bye, "q")


def colorList():
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "white"]
    return rnd.choice(colors)


tur.screensize(2000, 2000)
tur.bgcolor("black")

e = readFile()
for n in e:
    terminateProg()#Press q to quit the program

    tur.pencolor(colorList())#Get a random color and change the pen color

    moveDir = int(n) * 0.1 * 360
    tur.left(moveDir)
    tur.fd(20)

    tur.setheading(0)


tur.done()
