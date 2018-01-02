myList = [4,1,6,3,5,2]

def bubblesort(badList):
    length = len(badList)-1
    unsorted = True

    while unsorted:
        unsorted = False
        for i in range(0, length):
            if badList[i] > badList[i+1]:
                temp = badList[i]
                badList[i] = badList[i+1]
                badList[i+1] = temp
                unsorted = True

bubblesort(myList)
print myList
