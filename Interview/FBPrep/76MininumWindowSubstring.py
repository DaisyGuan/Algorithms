class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]

    def minWindow2(self, s, t):
        m = len(s)
        n = len(t)
        if m < n:
            return ''
        lt = {}
        for i in t:
            if i not in lt:
                lt[i] = 1
            else:
                lt[i] += 1
        missing = n
        i = I = J = 0
        for j, c in enumerate(s, 1):#enumberate from 1
            if c in lt and lt[c] > 0:
                missing -= 1
            if c in lt:
                lt[c] -= 1

            while i < j and not missing:
                if not J or j-i < J-I:
                    I, J = i, j
                if s[i] not in lt:
                    i += 1
                    continue
                else:
                    lt[s[i]] += 1
                    if lt[s[i]] > 0:
                        missing += 1
                    i += 1
        return s[I:J]

result = Solution()
re = result.minWindow2("ADOBECODEBANC", "ABC")
print re
#The current window is s[i:j] and the result window is s[I:J].
#In need[c] I store how many times I need character c (can be negative)
#and missing tells how many characters are still missing.
#In the loop, first add the new character to the window.
#Then, if nothing is missing, remove as much as possible from the window start and then update the result.
