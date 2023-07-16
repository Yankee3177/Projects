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

        ##if the sum is in the hashtable then you're stuck in a loop so return false.
        if summ in squares.values():
            return False
        ##The number is the key and the value would be the sum of that number.
        squares[str(num)] = summ
        x.clear()
        num = squares[str(num)]
        summ = 0

    if num == 1:
        return True

    return False

def containsDuplicate(nums) -> bool:
    table = {}
    #Looping through the param list.
    for num in range(len(nums)):
        #if num is in the dictionary then there's a duplicate
        if nums[num] in table:
            return True
        #the element in nums is the key and the value is the index(the loop number).
        table[nums[num]] = num

    return False

def containsNearbyDuplicate(nums, k) -> bool:
    table = {}
    for i in range(len(nums)):
        if nums[i] in table:
            if (i - table[nums[i]] <= k):
                return True

            if (i - table[nums[i]] > k):
                table[nums[i]] = i

        if nums[i] not in table:
            table[nums[i]] = i
    return False