def maxSubArray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        maxSum = currSum = nums[0]
        for num in nums[1:]:
            currSum = max(num, currSum + num)
            maxSum = max(maxSum, currSum)
        return maxSum

print maxSubArray([1,-2,4,7,3])
