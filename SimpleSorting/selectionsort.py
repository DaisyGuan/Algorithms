myList = [4,2,1,10,5,3,100]

def selectionsort(badList):
    length = len(badList)
    for i in range(0, length):
        subList=badList[i:]
        min_init=min(subList)
        index=badList.index(min_init)
        badList[index], badList[i] = badList[i],badList[index]

selectionsort(myList)
print myList
