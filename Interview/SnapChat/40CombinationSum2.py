class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        return self.search(candidates, 0 ,target)

    def search(self, candidates, start, target):
        if target==0:
            return [[]]
        res=[]
        for i in xrange(start,len(candidates)):
            if i!=start and candidates[i]==candidates[i-1]:
                continue
            if candidates[i]>target:
                break
            for r in self.search(candidates, i+1, target-candidates[i]):
                res.append([candidates[i]]+r)
        return res

#dp
class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        dp = [set() for i in xrange(target+1)]
        dp[0].add(())
        for num in candidates:
            for t in xrange(target, num-1, -1):
                for prev in dp[t-num]:
                    dp[t].add(prev + (num,))
        return list(dp[-1])
