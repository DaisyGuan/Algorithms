class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = s.split()
        print temp
        res = temp[::-1]
        return " ".join(res)


result = Solution().reverseWords("   love peace  ")
print result
