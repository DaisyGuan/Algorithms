class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #claim the result type
        result = [[]] #initiate result with the first []
        for num in nums:
            #loop result list, the only way to loop
            result += [item + [num] for item in result]
        return result

    def subsets2(self,nums):
        res = [[]]
        for num in nums:
            res += [item + [num] for item in res]
        # list is unhashable
        return list(set(tuple(sorted(t)) for t in res))


result = Solution()
re = result.subsets2([4,4,4,1,4])
print re
