class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        def isPalindrome(string):
            if string == string[::-1]:
                return True
            else:
                return False
        count = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if isPalindrome(s[i:j]):
                    count += 1
        return count
        
