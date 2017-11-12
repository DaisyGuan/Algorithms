class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lt = s.split()
        return len(lt[-1])



result = Solution()
re = result.lengthOfLastWord('Hello World')
print re
