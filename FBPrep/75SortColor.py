class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        #two pointers for 0 and 1
        for k in range(len(nums)):
            temp = nums[k]
            nums[k] = 2

            if temp < 2:
                nums[j] = 1
                j += 1
            if temp == 0:
                nums[i] = 0
                i += 1
        #no need to swap, just record and modify the value here
        #this is one pass algorithm
