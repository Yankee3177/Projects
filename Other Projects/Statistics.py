import random as rand

money = 200.00
expectedGain = 1.00 / 20
actualGain = 0.00
def cardGame(money):
    mon = money - 2.00
    won = False
    turns = 1
    myDict = dict()

    inList = False
    possibleNum = [1,2,3,4,5,6,7,8,9,10]
    userChoice = input("Enter a number between 1 and 20: ")

    for i in range(turns):

        myDict[i] = rand.choice(possibleNum)
        print(myDict[i] )
        if userChoice in myDict.values() :
            won = True
            mon += 3.00
            break

    return mon,won

counterWin = 0
counterLose = 0
win = False
for i in range(10):
    money,win = cardGame(money)

    if win:
        counterWin += 1
    else:
        counterLose += 1


    if money == 0.00:
        print("You're broke, go home!\n")
        break
    if money < 0.00:
        print("You owe ", abs(int(money)), " dollar\n")
        break

    print(money,"\n")

actualGain = 3 * (1 / 10) + (-2 * (9 / 10))
diff = actualGain - expectedGain
print(diff)
print("Wins..." , counterWin,"\n")
print("Losses...",counterLose, "\n")



