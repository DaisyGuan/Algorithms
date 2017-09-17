myList=[3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]

def quicksort(badList):
    quickSortHelper(badList,0,len(badList)-1)

def quickSortHelper(badList,start,end):
    if start < end:
        splitpoint = partition(badList,start,end)
        quickSortHelper(badList,start,splitpoint-1)
        quickSortHelper(badList,splitpoint+1,end)

def partition(badList,start,end):
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


quicksort(myList)
print myList
