def getPrimeFact(num):
    factors = []
    localNum = num
    for i in range(2,localNum+1):
        if localNum%i == 0 :
            factors.append(i)
            localNum /= i
    return factors

def gcd(a,b):

    aFactors = set(getPrimeFact(a))
    bFactors = set(getPrimeFact(b))

    commonFactors = aFactors.intersection(bFactors)
    prod = 1
    for fact in commonFactors:
        prod *= fact
    return prod



def euclidAlgo(a,b):
    if not a > b:
        a,b = b,a ##switches the a with b

    r = a%b
    while r > 0:
        a = b
        b = r
        r = a%b
    return b


print(euclidAlgo(3003,3003))