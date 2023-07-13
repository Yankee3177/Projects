alphList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
def encrypt(pText,key):
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

keyReady = False
textReady = False

while not textReady:
    plainText = input("Enter the information needed to encrypt, only letters are accepted:")

    if all(x.isalpha() or x.isspace() for x in plainText): ##This is to make sure only letters are passed in, spaces don't matter
        textReady = True
        break
    print("Only letters are accepted, try again ...")


while not keyReady:
    try :
        userKey = int(input("Enter the key you want to use for the encryption, it has to be between 1 and 25:"))

        while userKey < 1 or userKey > 25 :
            print("The key was not between 1 and 25, try again ...")
            userKey = int(input("Enter the key you want to use for the encryption, it has to be between 1 and 25:"))
        keyReady = True

    except:
        print("The key has to be a number, try again ... \n")

cList = encrypt(plainText.lower(),userKey)

cypherText = ''.join(cList)

print()

newUserKey = int(input("Enter the key needed to decrypt:"))

while newUserKey is not userKey:
    newUserKey = int(input("WRONGGG KEYYY!!! Try again:"))

decrypt(cypherText, newUserKey)
