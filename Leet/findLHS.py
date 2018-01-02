import collections

A=[1,3,5,7,9,11,13,15,15,16,17]
def findLHS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = collections.Counter(nums)
    ans = 0
    if len(count) == 1:
        return 0

    for x in count:
        j= x+1
        #print j
        if j not in count:
            ans = max(ans, 0)
            #ans = max(ans, count[x])
        if j in count:
            ans = max(ans, count[x]+count[x+1])
    return ans


print findLHS(A)
