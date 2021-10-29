def addMod(modNum):
    matrix = []
    for i in range(8):
        col = []
        for j in range(8):
            addition = i + j
            col.append(addition%modNum)
        matrix.append(col)
    return matrix

def printTable(matrix,length):
    for i in range(length):
        for j in range(length):
            print('{:7}'.format(matrix[i][j]), end='')
        print()

def multMod(modNum):
    matrix = []
    for i in range(8):
        col = []
        for j in range(8):
            mult = i * j
            col.append(mult % modNum)
        matrix.append(col)
    return matrix

resultAdd = addMod(8)
resultMult = multMod(8)

print("This is the Addition table: ")
printTable(resultAdd,8)
print('\n')
print("This is the Multiplication table: ")
printTable(resultMult,8)