def isPalindrome(num):
        """
        :type x: int
        :rtype: bool
        """
        return str(num) == str(num)[::-1]

print isPalindrome(12321)
