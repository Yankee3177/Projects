
primeNum = 0
hundreth = 100
bigGap = 0
gapSum = 0
primeList = []
gapList =[]

for num in range(1, 2001):

   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           primeNum += 1
           primeList.append(num)

           if num > hundreth:
               print()
               hundreth += 100


           print(num, end = ' ')


for nums in range(len(primeList)-1):

    gap = primeList[nums + 1] - primeList[nums]
    gapSum += gap

    if gap > bigGap:
        bigGap = gap
        continue

print()
averageGap = gapSum / primeNum -1

print("\nTotal Primes Found:" , primeNum)
print("\nThe average gap between Primes:", averageGap)
print("\nThe average gap rounded to the nearest hundreth is:",round(averageGap,2))
print("\nLargest gap between consecutive primes:", bigGap)