

newArr = []
secArr = []
message = open('abstractAlgebra.txt','r')
for line in message:
    newArr.append( line.strip('\n').split(',',2))

secArr = newArr[0][2].split(',')

for var in range(len(secArr)):
    secArr[var] = int(secArr[var])

print(secArr)