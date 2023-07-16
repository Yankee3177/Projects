import turtle as tur

tur.screensize(canvwidth=9000,canvheight=6000)
tur.speed(10)

def binConv(char):#Used to make the custom binary list
    vowelList = ['a','e','i','o','u']
    if char in vowelList:
        return 0
    return 1

def listConv(num):#Converting a string into a list.
    newList = []
    for i in num:
        newList.append(i)
    return newList

def horizontalLines(length):
    counter = 0
    while counter <= length:
        tur.pendown()
        tur.fd(20)# change this number to make it bigger or smaller
        tur.penup()
        counter+=1
        tur.fd(20)
    return counter

def verticalLines(length):
    counter = 0
    while counter <= (length//2)-1:
        tur.pendown()
        tur.fd(20)  # change this number to make it bigger or smaller
        tur.penup()
        counter += 1
        tur.fd(20)

maxlen = 30
lenPhrase = 0
binList = []
eulNum = "27182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274274663919320030599218174144"

while True :
    phrase = input("Enter a phrase no longer than 30 letters long: ").replace(" ","").lower()
    phrase = ''.join(filter(str.isalnum, phrase))#Eliminates all special characters
    lenPhrase = len(phrase)

    if lenPhrase > 0 and lenPhrase <= maxlen:
        break

for i in phrase:
    binList.append(binConv(i))

eulList = listConv(eulNum)
eulList = list(map(int,eulList))#Convert each char into an int


expand = 0
for n in range(lenPhrase):
    currY = int(tur.ycor())
    if binList[n] == 1:

        tur.penup()
        tur.goto(-200,expand)
        count = horizontalLines(lenPhrase)

    else:
        tur.penup()
        tur.goto(-180, expand)
        count = horizontalLines(lenPhrase)

    expand += 20

shift = -200
tur.left(90)

for i in range((count*2)+1):

    if eulList[i] %2 == 0:
        tur.goto(shift,0)
        verticalLines(lenPhrase)
    else:
        tur.goto(shift,20)
        verticalLines(lenPhrase)
    shift+=20

tur.done()
