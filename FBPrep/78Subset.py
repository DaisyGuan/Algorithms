class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
#a lot of corner case need to be considered
        for i in range(0,len(nums)):
            for j in range(i,len(nums)+1):
                    print nums[i:j]

    def subsets2(self,nums):
        #claim the result type
        result = [[]] #initiate result with the first []
        for num in nums:
            #loop result list, the only way to loop
            result += [item + [num] for item in result]
        return result


result = Solution()
re = result.subsets2([1,2,3])
print re
