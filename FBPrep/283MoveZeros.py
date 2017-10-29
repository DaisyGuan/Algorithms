#For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) != 0:
            zero = 0 #pointer points to the very first 0
            for i in range(0,len(nums)):
                if nums[i] != 0:
                    nums[i],nums[zero] = nums[zero],nums[i]
                    zero += 1 #record to first 0 in nums
        return nums



result=Solution()
re=result.moveZeroes([1,0,2,4,0,4,2])
print re
