
# def isPrime(num):
#     for i in range(2, num):
#         if (num % i) == 0:
#             return False
#     return True
#
# def print_factors(x):
#     primeFacts = []
#     print("The factors of", x, "are:")
#     for i in range(1, x + 1):
#         if x % i == 0:
#             print(i)
#             if isPrime(i):
#                 primeFacts.append(i)
#
#     return primeFacts


# def printPrimeFactorization(num):
#     workingNum = num
#     for div in range(2,workingNum+1):
#         exp = 0
#         while workingNum%div == 0:
#             exp += 1
#            ## print(div)
#             workingNum = workingNum/div
#         if exp != 0:
#             print(div, '^', exp,end=" * ")


def printPrimeFactorization(num):
    myDict={}

    workingNum = num

    for div in range(2, num+1):
        exp = 0
        while workingNum%div == 0:
            myDict.get(myDict[div]+1)
            workingNum = workingNum/ div



printPrimeFactorization(72)