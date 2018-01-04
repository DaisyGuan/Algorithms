class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        dp = [False] * (len(stones)+1)
        dp[0] = True
        dp[1] = True
        init = 1
        temp = 2
        while init < len(stones)+1 and dp[init] == True:
            if stones[init] + temp + 1 in stones:
                dp[init+1] = True
                temp = temp + 1

            if stones[init] + temp in stones:
                dp[init+1] = True

            if stones[init] + temp - 1 in stones:
                dp[init+1] = True
                temp = temp - 1

            init += 1

        return dp[-1]
