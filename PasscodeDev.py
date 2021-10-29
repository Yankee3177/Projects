from collections import defaultdict

def main():
    compAtt = [line.strip() for line in open('keylog.txt','r').readlines()]##This turns every number into a list item

    app = defaultdict(list)#This type of dict is a dict of lists, it will be used to avoid the keyerror. This will assign the keys with no values an empty list

    for attempt in compAtt:#loop through every keylog number.
        for i, n in enumerate(attempt):##This sorts each number in the list individually. The keys are the numbers that the passcode can be and the values are the positions
                                        ##where you can find that number.
            app[n].append(i)  ##n is the number and i is the index where that number is at

    averagePositions = {} ##This dictionary is going to be used to store the average position of each individual number

    for k,v in list(app.items()):##This will loop through every number in the appearances dict and get the average
        averagePositions[k] = float(sum(v))/float(len(v))## of the positions that number has been in.It'll then store that number with it's average
                                                         ## in the new averagePositions dict.The reason why it's a float is because
                                                         #I'll be sorting it from least to greatest and that's how I will know the order of the numbers.

    answerList = [k for k,v in sorted(list(averagePositions.items()), key=lambda a: a[1])]#it'll first turn the dict into a list and then you will use the average
       #the k value is what's being stored in the list a                         # to sort it out from least to greatest. The key is what's being used
                                                                                 #to use the average as the deciding factor since when you convert the
                                                                                 #dict to a list the first value in the list,list[0], is the number and list[1] is the average.

    print(''.join(str(x) for x in answerList))#Loop through the list and concatenate the numbers, this will give us the final result.


main()# Call main