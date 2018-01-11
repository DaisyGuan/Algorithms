#param s string
#param return int
def longessSameSub(mystr):

    latestChar = ""
    currLen = 0
    maxLen = 0

    for c in mystr:
        if c == latestChar:
            currLen += 1
            maxLen = max(maxLen, currLen)
        else:
            currLen = 1
            latestChar = c

    return maxLen

print longessSameSub('aaabcaaaaaaba')
