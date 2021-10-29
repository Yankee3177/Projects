def binaryConverter(str):
    modStr = str
    res = ''.join(format(i,'b')for i in bytearray(modStr, encoding = 'utf8'))
    return res


def copyList(list):
    listt = []
    for var in list:
        listt.append(var)
    return listt

def plainTextConverter(str):
    modStr = str
    string = ""
    for i in range(0,len(modStr),7):
        temp = modStr[i:i+7]
        decimal = int(temp,2)
        string += chr(decimal)
    return string


def encrypt(pText,pKey):
    modText = binaryConverter(pText)
    cList = list(modText)
    newList = copyList(cList)
    index = pKey - 1
    print(''.join(cList))

    if len(cList) % pKey != 0:
        counter = index
        while counter < len(cList):
            minusBit = cList[counter - 1]
            actualBit = cList[counter]

            newList[counter] = minusBit
            newList[counter - 1] = actualBit
            counter += pKey
        # For the edge case I'm switching the last number with the first number
        firstNum = cList[0]#Store the first num
        lastNum = cList[len(cList) - 1]#Store the last num

        newList[0] = lastNum#set the first number to the value of the last number
        newList[len(newList) - 1] = firstNum#set the last number to the value of the first number
    else:
        counter = index
        while counter < len(cList):
            minusBit = cList[counter - 1]
            actualBit = cList[counter]

            newList[counter] = minusBit
            newList[counter - 1] = actualBit
            counter += pKey
    return ''.join(newList)

def decrypt(cText, pKey):
    cList = list(cText)
    newList = copyList(cList)
    counter = pKey - 1

    if len(cList) % pKey != 0:
        while counter < len(cList):
            minusBit = cList[counter - 1]
            actualBit = cList[counter]

            newList[counter] = minusBit
            newList[counter - 1] = actualBit
            counter += pKey
        # For the edge case I'm switching the last number with the first number
        firstNum = cList[0]#Store the first num
        lastNum = cList[len(cList) - 1]#Store the last num

        newList[0] = lastNum#set the first number to the value of the last number
        newList[len(newList) - 1] = firstNum#set the last number to the value of the first number

    while counter < len(cList):
        minusBit = cList[counter - 1]
        actualBit = cList[counter]

        newList[counter] = minusBit
        newList[counter - 1] = actualBit
        counter += pKey

    ans = plainTextConverter(''.join(newList))
    return ''.join(ans)

plainText = input("Enter the information needed to encrypt:")
userKey = int(input("Enter the key you want to use for the encryption:"))

print("This is the plainText:",plainText)
cText = encrypt(plainText,userKey)
print(cText)

res = decrypt(cText,userKey)
print("This is the result of the decrypt",res)
