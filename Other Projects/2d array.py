a = [[1,2,3],[3,2,1]]
b = [[1,0],[1,0],[1,0]]
p = [[6,0],[6,0]]

if len(a) != len(b[0]):
    print("Dimensions are unacceptable for matrix Multiplication")
    quit()

def getRowInProduct():
    for out in range(len(a)):
        for i in range(len(b[0])):
            summ = 0
            for j in range(len(b)):
                summ += a[i][j] * b[j][i]
            print(summ,end=" ")
        print()

getRowInProduct()