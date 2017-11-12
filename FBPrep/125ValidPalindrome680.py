class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l,r = 0, len(s) -1
        while l < r:
            #Return true if all characters in the string are alphanumeric and there is at least one character, false otherwise.
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    #if I could delete one character
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        while i < len(s)/2 and s[i] == s[-(i+1)]:
            i += 1

        s = s[i:len(s) - i]#only left different part
        #return result : drop edge and test respectively
        return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1]

x = Solution()
result = x.validPalindrome('abs')
#print result
s = 'abcbda'
print s[1:len(s)-1]
m = s[1:len(s)-1]
print m[1:],m[1:][::-1]
print m[:-1],m[:-1][::-1]
