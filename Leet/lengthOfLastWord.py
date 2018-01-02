def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    #count = 0
    i = 0
    while len(s) != 0 and s[-(i+1)] == ' ':
        s = s[:-1]
    while i != len(s) and s[-(i+1)] != ' ':
            i += 1
    return i

s='a adadfd '
#print s[:-1]
print lengthOfLastWord('adfa adadfd')
