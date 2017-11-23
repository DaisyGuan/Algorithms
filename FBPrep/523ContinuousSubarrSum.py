class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            for i in range(len(nums)-1):
                print i
                if nums[i] == 0 and nums[i+1] == 0:
                    return True
        else:
            for i in range(len(nums)-1):
                for j in range(i+2, len(nums)+1):
                    #print i, j
                    if sum(nums[i:j]) % abs(k) == 0:
                        return True
                    else:
                        continue

            return False

result = Solution().checkSubarraySum([0,0], -1)
print result

print 0%1
