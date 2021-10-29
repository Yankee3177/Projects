def printList(list):
    for nums in list:
        print(nums)



f = open("keylog.txt", 'r')
keyys = []
for x in f:
 keyys.append(x.strip())


for a in range(len(keyys)):
    keyys[a] = list(map(int, str(keyys[a])))



printList(keyys)