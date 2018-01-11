class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfshelper(candidates,target, 0, [], res)
        return res


    def dfshelper(self, candidates, target, index, path, res):
        if target < 0:
            return
        elif target == 0:
            res.append(path)
            return
        for i in range(index, len(candidates)):
            self.dfshelper(candidates, target-candidates[i], i, path+[candidates[i]], res)


#dp
def combinationSum(self, candidates, target):
    candidates.sort()
    dp = [[[]]] + [[] for i in xrange(target)]
    for i in xrange(1, target + 1):
        for number in candidates:
            if number > i:
                break
            for L in dp[i - number]:
                if not L or number >= L[-1]:
                    dp[i] += L + [number],
    return dp[target]
