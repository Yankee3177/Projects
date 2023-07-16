'''
This program uses basic abstract alegebra terminology to determine if the input is a group, field, ring.
'''


def closureAdd(testArr,realNums):
    '''

    :param testArr:
    :param realNums:
    :return: True or False depending on the previous calculations
    '''
    temp = 0
    test = 0
    closure = False
    for i in range(len(testArr) - 1 ):
        temp = testArr[i]
        test = testArr[i + 1]

        calc = temp + test

        for var in testArr:
            if var == calc:
                closure = True
                break
            else:
                if realNums:
                    intNum = isinstance(var,int)
                    floatNum = isinstance(var,float)
                    if intNum or floatNum:
                        closure = True
                        break
                else:
                    closure = False

        if closure == False:
            return closure

    return closure

def closureMult(testArr,realNums):
    temp = 0
    test = 0
    closure = False
    for i in range(len(testArr)-1):
        if i + 1 > len(testArr):
            break
        temp = testArr[i]
        test = testArr[i + 1]

        calc = temp * test

        for var in testArr:
            if var == calc:
                closure = True
                break
            else:
                if realNums:
                    intNum = isinstance(var, int)
                    floatNum = isinstance(var, float)
                    if intNum or floatNum:
                        closure = True
                        break
                else:
                    closure = False

        if closure == False:
            return closure

    return closure


def associativeAdd(testArr):
    a = 0
    b = 0
    c = 0

    associative = False
    for i in range(len(testArr) - 2):
        a = testArr[i]
        b = testArr[i + 1]
        c = testArr[i + 2]

        calc = a + (b + c)

        calc2 = (a + b) + c

        if calc == calc2:
            associative = True
        else:
            associative = False
            return associative
    return associative

def associativeMult(testArr):
    a = 0
    b = 0
    c = 0

    associative = False
    for i in range(len(testArr) - 2):
        a = testArr[i]
        b = testArr[i + 1]
        c = testArr[i + 2]

        calc = a * (b * c)

        calc2 = (a * b) * c

        if calc == calc2:
            associative = True
        else:
            associative = False
            return associative
    return associative

#this is the property of additive identity
def identityAdd(testArr):
    ident = False

    for var in testArr:
        if var == 0:
            ident = True
            return ident
    return ident

def identityMult(testArr):
    ident = False

    for var in testArr:
        if var == 1:
            ident = True
            return ident
    return ident

def inverseAdd(n):
    nums = n
    calc = 0
    isInverse = False
    for var in nums:
        calc = -(var)
        for num in nums:
            if num == calc:
                isInverse = True
                break
            else:
                isInverse = False
        if isInverse == False:
            return isInverse
    return isInverse

def inverseMult(n):
    nums = n
    calc = 0
    isInverse = False
    for var in nums:
        if var == 0:
            isInverse = False
            break
        calc = var ** -1
        for num in nums:
            if calc == num:
                isInverse = True
                break
            else:
                isInverse = False
        if isInverse == False:
            return isInverse
    return isInverse

def commutativeAdd(n):
    testArr = n
    isCommutative = False
    for i in range(len(testArr)):
        a = testArr[i]
        for num in range(len(testArr) - 1):
            b = testArr[num+1]

            calc = a + b
            test = b + a
            if calc == test :
                isCommutative = True
            else:
                isCommutative = False
                break
        if isCommutative == False :
            return isCommutative

    return isCommutative


def commutativeMult(n):
    testArr = n
    isCommutative = False
    for i in range(len(testArr)):
        a = testArr[i]
        for num in range(len(testArr) - 1):
            b = testArr[num + 1]

            calc = a * b
            test = b * a
            if calc == test:
                isCommutative = True
            else:
                isCommutative = False
                break
        if isCommutative == False:
            return isCommutative

    return isCommutative

def distribute(n):
    testArr = n
    isDistributive = False

    for i in range(len(testArr)):
        a = testArr[i]
        for var in range(len(testArr)-1):
            b = testArr[var+1]
            for num in range(len(testArr) - 2):
                c = testArr[num+ 2]
                calc = a*(b+c)
                test = (a*b) + (a*c)

                secCalc = (a+b)*c
                secTest = (a*c) + (b*c)

                if calc == test and secCalc == secTest:
                    isDistributive = True

                else:
                    isDistributive = False
                    return isDistributive
    return isDistributive


def machine(operation,realNums,numListArr):
    group = False
    ring = False
    field = False

    closure = False
    associative = False
    identity = False
    commutative = False
    inverse = False
    multClosure = False
    associMult = False
    distributive = False
    multCommutative = False
    multIdentity = False
    multInverse = False

    if operation == 'addition':

        closure = closureAdd(numListArr,realNums)
        associative = associativeAdd(numListArr)
        identity = identityAdd(numListArr)
        inverse = inverseAdd(numListArr)
        commutative = commutativeAdd(numListArr)
        multClosure = closureMult(numListArr,realNums)
        associMult = associativeMult(numListArr)
        distributive = distribute(numListArr)
        multCommutative = commutativeMult(numListArr)
        multIdentity = identityMult(numListArr)
        multInverse = inverseMult(numListArr)

        if closure == True and associative == True and identity == True and inverse == True:
            group = True
        if group == True and commutative == True and multClosure == True and associMult == True and distributive == True:
            ring = True
        if group == True and ring == True and multCommutative == True and multIdentity == True and multInverse == True:
            field = True




    else:
        multClosure = closureMult(numListArr, realNums)
        associMult = associativeMult(numListArr)
        multIdentity = identityMult(numListArr)
        multInverse = inverseMult(numListArr)
        multCommutative = commutativeMult(numListArr)
        distributive = distribute(numListArr)

        if multClosure == True and associMult == True and multIdentity == True and multInverse == True:
            group = True
        if group == True and distributive == True:
            ring = True
        if group == True and ring == True and multCommutative == True:
            field == True


    if group == True and ring == False and field == False:
        print(numListArr)
        print("This is a group under" , operation)

    elif group == True and ring == True and field == False:
        print(numListArr)
        print("This is a ring under" , operation )

    elif group == True and ring == True and field == True:
        print(numListArr)
        print("This is a field under", operation)

    else:
        print(numListArr)
        print("This is not a group,ring or field under" , operation)

    return 'done'



newArr = []
secArr = []
message = open('abstractAlgebra.txt','r')
for line in message:
    newArr.append( line.strip('\n').split(',',2))

for cases in range(len(newArr)):
    secArr = newArr[cases][2].split(',')

    for var in range(len(secArr)):
        try:
            secArr[var] = int(secArr[var])
        except:
            secArr[var] = float(secArr[var])

    machine(newArr[cases][0],newArr[cases][1],secArr)
    print("\n")




