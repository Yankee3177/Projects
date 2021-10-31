def isHappy(n:int) -> bool:
    num = n
    """
    :type n: int
    :rtype: bool
    """
    summ = 0
    squares = {}
    while num > 1:
        x = [int(a) for a in str(num)]  ## This will split each digit and store into a list
        for i in x:  ## Traverse through the whole list and square each digit
            summ += i ** 2
        if summ in squares.values():
            return False
        squares[str(num)] = summ  ##The number is the key and the value would be the sum of that
        ##number.
        x.clear()
        num = squares[str(num)]

        summ = 0

    if num == 1:
        return True

    return False


print(isHappy(94))