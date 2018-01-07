class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if not s:
            return []

        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
                for item in resultOfTheRest:
                    #print item
                    item = word + ' ' + item
                    #print item, res
                    res.append(item)
                    #print res
        #print res
        memo[s] = res
        print memo


        return res


result = Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
print result
