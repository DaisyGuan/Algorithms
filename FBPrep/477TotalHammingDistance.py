class Solution(object):
    def hammingDistance(self, x, y):
        return bin(x^y).count('1')
    total = 0
    def totalHamming(self, nums):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                total += hammingDistance(nums[i], nums[j])
        return total

class Solution2(object):
    class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bits = [[0,0] for _ in range(32)]

        for x in nums:
            for i in range(32):
                bits[i][x%2] += 1
                x /= 2
        return sum(x*y for x, y in bits)
