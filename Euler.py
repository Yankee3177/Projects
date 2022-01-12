def isPrime(num):
     for i in range(2, num):
         if (num % i) == 0:
             return False
     return True


def eul(n):
    y = n
    for i in range(2,n+1):
        if isPrime(i) and n % i  == 0 :
            y -= y/i
    return int(y)

def average(list):
    summ = 0
    for var in list:
        summ += var
    return summ/(len(list))

mostPhiNum = 0
eulCalc = 0
summ = 0
eulList = []


print(eul(2))
'''
for i in range(1,1001):
    eulNum = 0
    eulNum = eul(i)
    if eulNum > mostPhiNum:
        eulCalc = i
        mostPhiNum = eulNum
    eulList.append(eulNum) 
    summ += eulNum
    print(i,eulNum,sep=" ")


print('\nThis is the number with the most positive integers that are less than it and relatively prime to it: ', eulCalc)
print("This number has this amount of numbers less than it that are relatively prime to it: ", mostPhiNum)
print("\nThe average of all the prime numbers less than the value of n, when n was all the numbers starting from 1 up to 1000:",average(eulList))
print("\nThis is the total amount of prime numbers less than the value of n, using the numbers from 1 to 1000:",summ)

'''


