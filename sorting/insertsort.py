myList=[3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]

def insertsort(badList):
    length = len(badList)
    for i in range(0,length):
        j = i
        while j > 0 and badList[j-1] > badList[j]:
            badList[j-1],badList[j] = badList[j],badList[j-1]
            j -= 1

insertsort(myList)
print(myList)
