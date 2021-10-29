def binaryToDecimal(listt):
    newStr = ''.join(listt)
    decimal = int(newStr, 2)
    return decimal

def decimalToBinary(num):
    return bin(num).replace("0b", "")

def split(word):
    return [char for char in word]

def fixLen(newLen,listt):
    newList = []
    chList = listt

    for i in range(newLen):
        newList.append('0')

    for i in range(len(chList)):
        newList.append(chList[i])

    return newList


def xor(x,y):
    binX = split(decimalToBinary(x))
    binY = split(decimalToBinary(y))
    newBin = []

    if len(binX) > len(binY):
        fixNum = len(binX) - len(binY)
        binY = fixLen(fixNum,binY)

    if len(binY) > len(binX):
        fixNum = len(binY) - len(binX)
        binX = fixLen(fixNum,binX)

    length = len(binX)

    for i in range(length):
        if binX[i] == binY[i]:
            newBin.append('0')
        else:
            newBin.append('1')
    return binaryToDecimal(newBin)

def encrypt(message, key):
    messageList = []

    for i in range(len(message)):
        messageList.append(xor(message[i],key[i]))

    return messageList

def isEnglish(ascii1, ascii2):
    xorNum = xor(ascii1,ascii2)

    if 32 <= xorNum and xorNum >=90 :
        return True
    elif 97<= xorNum and xorNum <= 122 :
        return True
    return False

def letters(indexx, cipher):
    letter = []
    for i in range(indexx, len(cipher), 3):
        letter.append(cipher[i])
    return letter

def isLetter(letters):
    actLett = []
    eng_letters = []
    for i in range(97, 124):
        eng_letters.append(i)

    for j in eng_letters:
        for i in range(len(letters)):
            if isEnglish(letters[i],j):
                actLett.append(j)
    return actLett

message = open('cipher.txt').read().split(',')

for i in range(len(message)):
    message[i] = int(message[i])

ans1 = letters(0,message)
print(ans1,'\n')
ans2 = letters(1,message)
print(ans2,'\n')

ans3 = letters(2,message)
print(ans3)

##Speed is reduced because you'll have more permutations. As a result the program has to encrypt and decrypt largers chunks of data the larger block sizes you
#have

