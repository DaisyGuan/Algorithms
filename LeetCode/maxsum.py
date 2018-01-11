#l is a list of nums
def maxSum(nums):
    currSum=0
    maxSum=0
    for i in range(0,len(nums)):
        currSum += nums[i]
        if currSum < 0:
            currSum = 0
        if maxSum < currSum:
            maxSum = currSum
    return maxSum
#have problem with single input and none
