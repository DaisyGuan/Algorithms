#The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#Given two integers x and y, calculate the Hamming distance.
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')


result = Solution()
re = result.hammingDistance(1,10)

print re

#running time:logx+logy+comparison. (logn)
