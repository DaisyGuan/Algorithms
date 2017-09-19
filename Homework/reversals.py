import random

def reversalCount(alist):
    recount = 0
    for i in range(len(alist)-1):
        for j in range(i,len(alist)):
            if alist[i] > alist[j]:
                recount += 1
    return recount

newlist = random.sample(range(4),4)
print newlist

print reversalCount([1,2,3,4])
