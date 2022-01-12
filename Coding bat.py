for i in range(1,999999999999999999):
    summ=0
    for char in str(i):
        num = int(char)
        summ += pow(num,num)
    if summ == i:
        print("Found one of these special numbers...", i)