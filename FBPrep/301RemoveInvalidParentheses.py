#Remove the minimum number of invalid parentheses
#in order to make the input string valid. Return all possible results.
#Note: The input string may contain letters other than the parentheses ( and ).
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isvalid(s):
            ctr = 0
            for c in s:
                if c == '(':
                    ctr += 1
                elif c == ')':
                    ctr -= 1
                    if ctr < 0:
                        return False#)))))))))((((((((v
            return ctr == 0

        level = {s}#set {}
        while True:
            valid = filter(isvalid, level)# level after filtered
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}#iteration#every time reduce 1 symbol

result = Solution()
re = result.removeInvalidParentheses('()((()')
print re
