class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        i, j = 0, 0
        res = len(nums) + 1
        total = 0

        while total < s:
            total += nums[j]
            j += 1
            while total >= s:
                if j-i < res:
                    res = j - i
                total -= nums[i]
                i += 1

            if j == len(nums):
                break

        if res > len(nums):
            return 0

        return res
                    
