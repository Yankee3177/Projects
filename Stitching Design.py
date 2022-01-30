import turtle as tur

tur.speed(10)
def binConv(char):
    vowelList = ['a','e','i','o','u']
    if char in vowelList:
        return 0
    return 1

def listConv(num):
    newList = []
    for i in num:
        newList.append(i)
    return newList

def horizontalLines(length):
    counter = 0
    while counter <= length:
        tur.pendown()
        tur.fd(20)# change this number to make it bigger
        tur.penup()
        counter+=1
        tur.fd(20)

def verticalLines(length,numType):#1 is for odd numbers and 2 is for even numbers
    counter = 0
    if numType == 1:
        while counter <= (length//2):
            tur.pendown()
            tur.fd(20)  # change this number to make it bigger
            tur.penup()
            counter += 1
            tur.fd(20)
    else:
        while counter <= (length//2):
            tur.pendown()
            tur.fd(20)  # change this number to make it bigger
            tur.penup()
            counter += 1
            tur.fd(20)


maxlen = 30
lenPhrase = 0
binList = []
eulNum = "27182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274274663919320030599218174144"
while True :
    phrase = input("Enter a phrase no longer than 30 letters long: ").replace(" ","").lower()
    lenPhrase = len(phrase)
    if lenPhrase > 0 and lenPhrase <= maxlen:
        break
for i in phrase:
    binList.append(binConv(i))

eulList = listConv(eulNum)
eulList = list(map(int,eulList))#Convert each char into an int

largeY = 0
expand = 0
for n in range(lenPhrase):
    currY = int(tur.ycor())
    if binList[n] == 1:

        tur.penup()
        tur.goto(0,expand)
        horizontalLines(lenPhrase)

    else:
        tur.penup()
        tur.goto(20, expand)
        horizontalLines(lenPhrase)

    currY = int(tur.ycor())
    if currY > largeY:
        largeY = currY
    expand += 20
    print(expand)

shift = 0
tur.left(90)
for i in range(largeY+1):

    if eulList[i] %2 == 0:
        tur.goto(shift,0)
        verticalLines(lenPhrase,2)
    else:
        tur.goto(shift,20)
        verticalLines(lenPhrase,1)
    shift+=20

tur.done()
