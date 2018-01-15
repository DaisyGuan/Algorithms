class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        currLen = 0
        maxLen = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if sum(nums[i:j+1]) == k:
                    currLen = j-i+1

            maxLen = max(maxLen, currLen)

        return maxLen

#running time O(n^2)
    def maxSubArrayLen2(self,nums, k):
        sum_table = {} # key: sum(nums[:i+1]), value: i
        total = 0
        max_len = 0
        for i in range(0, len(nums)):
            total += nums[i]
            if not sum_table.has_key(total):
                sum_table[total] = i
            remain = total - k
            if remain == 0:
                max_len = max(i+1, max_len)
            elif sum_table.has_key(remain):
                max_len = max(i - sum_table[remain], max_len)

        return max_len
