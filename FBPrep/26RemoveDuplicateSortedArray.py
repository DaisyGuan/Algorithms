#class Solution(object):
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    newTail = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[newTail]:
            newTail += 1
            nums[newTail] = nums[i]

    return newTail + 1


#result = Solution()
#re = result.removeDuplicates([1,1,2])
#print re

print removeDuplicates([1,1,2])

def removeDuplicates2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    newList = []

    for element in nums:
        if element not in newList:
            newList.append(element)

    result = len(newList)
    return result

print removeDuplicates2([1,1,2])

def removeDuplicatefromString(strs):
        """
        :type nums: str
        :rtype: str
        """
        newList = []
        for s in strs:
            if s not in newList:
                newList.append(s)
        return ''.join(newList)
print removeDuplicatefromString('ababs')
