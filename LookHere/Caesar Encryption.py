
def encrypt(pText,key):
    alphList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    newSentence = []

    sentence = pText
    moveMent = key

    for element in range(0, len(sentence)):
        letter = sentence[element]

        if letter == ' ':
            print(letter, end = "")
            newSentence.append(letter)
            continue

        position = alphList.index(letter)

        # if moveMent > 25:
        #     anss = moveMent - position
        #     newPos = 25 - anss
        #     print(alphList[newPos + 1], end = "")
        #     newSentence.append(alphList[newPos + 1])
        #     continue

        if position + moveMent > 25:
            ans = 25 - position
            newPosition = ans - moveMent
            let = abs(newPosition)
            print(alphList[let - 1], end = "")
            newSentence.append(alphList[let - 1])
            continue

        newLetter = position + moveMent

        print(alphList[newLetter], end = "")
        newSentence.append(alphList[newLetter])

    return newSentence

def decrypt(cText,key):
    alphList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    sentence = cText
    moveMent = key

    for element in range(0, len(sentence)):
        letter = sentence[element]

        if letter == ' ':
            print(letter, end="")
            continue

        position = alphList.index(letter)
        if position - moveMent < 0:
            ans = position - moveMent
            newPos = 25 - abs(ans)
            print(alphList[newPos + 1], end="")
            continue
        newLetter = position - moveMent

        print(alphList[newLetter], end="")


def listToString(s):
    str1 = ""

    for ele in s:
        str1 += ele

    return str1


plainText = input("Enter the information needed to encrypt:").lower()
userKey = int(input("Enter the key you want to use for the encryption, it has to be between 1 and 25:"))

while userKey < 1 or userKey > 25 :
    userKey = int(input("Enter the key you want to use for the encryption, it has to be between 1 and 25:"))

cList = encrypt(plainText,userKey)

cypherText = listToString(cList)

print()

newUserKey = int(input("Enter the key needed to decrypt:"))

while newUserKey is not userKey:
    newUserKey = int(input("WRONGGG KEYYY!!! Try again:"))

decrypt(cypherText, newUserKey)
