import random
myList=[3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]

def randomquicksort(badList):
    randomQuickSortHelper(badList,0,len(badList)-1)

def randomQuickSortHelper(badList,start,end):
    if start < end:
        splitpoint = partition(badList,start,end)
        randomQuickSortHelper(badList,start,splitpoint-1)
        randomQuickSortHelper(badList,splitpoint+1,end)

    return badList

def partition(badList,start,end):
    randompivot = random.choice(badList[start:end+1])
    randomindex = badList.index(randompivot)
    badList[start],badList[randomindex] = badList[randomindex],badList[start]
    pivotvalue=badList[start]
    leftindex=start+1
    rightindex=end
    done = False
    while not done:
        while leftindex <= rightindex and badList[leftindex] <= pivotvalue:
            leftindex += 1

        while rightindex >= leftindex and badList[rightindex] >= pivotvalue:
            rightindex -= 1

        if rightindex < leftindex:
            done = True
        else:
            badList[leftindex],badList[rightindex]=badList[rightindex],badList[leftindex]

    badList[start],badList[rightindex]=badList[rightindex],badList[start]

    return rightindex

randomquicksort(myList)
print myList
