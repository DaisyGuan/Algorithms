import unittest
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)
        max_len = i = 0
        #print len(nums)
        while i < len(nums):
            curr = 1
            while i + 1 < len(nums) and nums[i] < nums[i + 1]:
                curr, i = curr + 1, i + 1
            max_len = max(max_len, curr)
            i += 1
            #print i
        return max_len

result = Solution().findLengthOfLCIS([1,2,3,2,6,7,8,9,10,11,12,1,2,3])
print result

#class Test(unittest.TestCase):
#    def Case1(self):
    #    print Solution().findLengthOfLCIS([1,2,3,5,7])

#if __name__ == '__main__':
#    unittest.main()
