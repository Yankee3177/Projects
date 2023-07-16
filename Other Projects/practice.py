import turtle as tur
import math
tur.circle(100)
tur.left(90)
tur.forward(100)
myList = [tur.pos()]
print(myList[0])
print(round(myList[0][0]))
tur.goto(0,0)
tur.goto(myList[0])
tur.done()