def isPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False

    return True


def primee(num):
    if num % 2 == 0:
        return False

    return True


def getPrimeFactors(num):
    listt = []
    for i in range(2,num):
        while num %i == 0:
            listt.append(i)
            num = num//i
    return listt


def gcd(a,b):

    aFactors = set(getPrimeFactors(a))
    bFactors = set(getPrimeFactors(b))

    commonFactors = aFactors.intersection(bFactors)
    prod = 1
    for fact in commonFactors:
        prod *= fact
    return prod


def gcdofList(listt):
    for i in range(listt[0],0,-1):
        passes = True
        for item in listt:
            if item%i != 0:
                passes = False
                break
        if passes:
            return i



def isRelativelyPrime(a,b):
    if gcdofList([a,b]) == 1 :
        return True
    return False

def reduceFraction(num,den):
    div = gcdofList([num,den])
    return str(num//div) + "/" +str(den//div)

def eul(n):##Phi num
    y = n
    for i in range(2,n+1):
        if isPrime(i) and n % i  == 0 :
            y -= y/i
    return int(y)



print(reduceFraction(50,99))
'''
#A number is either prime or composite(product of primes)
        
'''

