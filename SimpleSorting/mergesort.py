myList = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]

def mergesort(badList):
    if len(badList)>1:
        mid = len(badList)//2
        lefthalf = badList[:mid]
        righthalf = badList[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                badList[k]=lefthalf[i]
                i=i+1
            else:
                badList[k]=righthalf[j]
                j=j+1
            k=k+1
        #len(left)>len(right), only rest of left
        while i < len(lefthalf):
            badList[k]=lefthalf[i]
            i=i+1
            k=k+1

        #len(left)<len(right), only rest of right
        while j < len(righthalf):
            badList[k]=righthalf[j]
            j=j+1
            k=k+1

mergesort(myList)
print(myList)
