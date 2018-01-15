class Solution(object):
    def threeSum(self,nums):
        """
        :type nums: List[int]
        : rtype: List[List[int]]
        """
        if len(nums) < 3:
                return []
        elif len(nums) == 3:
            if sum(nums) == 0:
                return [sorted(nums)]

        nums = sorted(nums)
        ans = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: # avoid duplication, solve time limit, first 0,have j,k
                continue
            j = i+1
            k = len(nums) - 1

            while j < k:
                if j > i + 1 and nums[j] == nums[j-1]: # avoid duplication
                    j += 1
                    continue
                if k < len(nums) - 1 and nums[k] == nums[k+1]: # avoid duplication
                    k -= 1
                    continue

                temp_sum = nums[i] + nums[j] + nums[k]
                if temp_sum == 0:
                    ans.append([nums[i],nums[j],nums[k]])

                if temp_sum > 0:
                    k -= 1
                else:
                    j += 1
        #skt = list(set(tuple(i) for i in ans))
        #set for reducing duplication
        # set need iterate on j
        return ans

        #Lists are enclosed in brackets: can be changed
        #Tuples are enclosed in parentheses:immutable
        #Dictionaries are built with curly brackets:
        #Sets are made using the set() builtin function. for duplication


#running time O(n^2)
    def threeSum2(self,nums):
        if len(nums) <3:
             return []
        elif len(nums) == 3:
            if sum(nums) == 0:
                return [sorted(nums)]

        nums.sort()
        res =[]

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: # avoid duplication
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k:
                if j > i + 1 and nums[j] == nums[j-1]: # avoid duplication
                    j += 1
                    continue
                if k < len(nums) - 1 and nums[k] == nums[k+1]: # avoid duplication
                    k -= 1
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i],nums[j],nums[k]])
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1

        return res

result = Solution()
re = result.threeSum([1,0,0,0,-2,0,1,1,2])
print re
