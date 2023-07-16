import random

alphList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
charKeys = []

for nums in range(26):
    charKeys.append(random(1,26))

def encrypt(pTextt,keys):
    cypher = ""

    for letter in pTextt:
        index = alphList.index(letter)
        cypher += charKeys[index]

    return cypher

def decrypt(cText, key) :
    pText = ""

    for letter in cText:
        pText += alphList[charKeys.index(letter)]

    return pText


print(encrypt("Hiiiiiiiiii", charKeys))
result = encrypt("Hiiiiiiiiii", charKeys)

print(decrypt(result,charKeys))


