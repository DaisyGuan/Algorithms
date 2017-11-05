class Solution(object):
    #d is an array that contains booleans
    #d[i] is True if there is a word in the dictionary that
    #ends at ith index of s AND d is also True at the beginning of the word
    def wordBreak(self, s, wordDict):
        d = [False] * len(s)
    	for i in range(len(s)):
    		for w in wordDict:
    			if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                    #for the last true and first one is true
    				d[i] = True
    	return d[-1]
    #return solution
    def wordBreak2(self, s, wordDict):
        memo = {len(s): ['']}
        def sentences(i):
            if i not in memo:
                memo[i] = []
                for j in range(i+1, len(s)+1):
                    if s[i:j] in wordDict:
                        for tail in sentences(j):
                            if tail != '':
                                memo[i].append(s[i:j] + ' ' + tail)
                            else:
                                memo[i].append(s[i:j])
                """
                memo[i] = [s[i:j] + (tail and ' ' + tail)
                           for j in range(i+1, len(s)+1)
                           if s[i:j] in wordDict
                           for tail in sentences(j)]
                """
            #print memo
            return memo[i]

        return sentences(0)

    def wordBreakFindMinBreak(self, s, wordDict):
        memo = {len(s): ['']}
        def sentences(i):
            if i not in memo:
                memo[i] = []
                for j in range(i+1, len(s)+1):
                    if s[i:j] in wordDict:
                        for tail in sentences(j):
                            if tail != '':
                                memo[i].append(s[i:j] + ' ' + tail)
                            else:
                                memo[i].append(s[i:j])
                """
                memo[i] = [s[i:j] + (tail and ' ' + tail)
                           for j in range(i+1, len(s)+1)
                           if s[i:j] in wordDict
                           for tail in sentences(j)]
                """
            return memo[i]

        for i in range(len(sentences(0))):
            minBreak = 100000000
            currMinBreak = min(minBreak,len(sentences(0)[i])-len(s))
        return currMinBreak

        #return sentences(0)



result = Solution()
re = result.wordBreak("leetcode",["leet","code"])
re2 = result.wordBreak2("leetcodegood",["leet","code","good","leetcode", "leetcodegood"])
re3 = result.wordBreakFindMinBreak("leetcodegood",["leet","code","good","leetcode", "leetcodegood"])
#print re1
print re2
print re3
