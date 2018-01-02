class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] != t[i]:
                    return s[i+1:] == t[i+1:]
                    break
            else:
                return False
        elif abs(len(s)-len(t)) == 1:
                for j in range(min(len(s), len(t))):
                    if s[j] != t[j]:
                        return s[j+1:] == t[j:] or s[j:] == t[j+1:]
                        break
                else:
                    return True
        else:
            return False


result = Solution()
re = result.isOneEditDistance('ab','ac')
print re
