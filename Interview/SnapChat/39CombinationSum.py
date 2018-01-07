class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self. dfshelper(candidates,target, 0, [], res)
        return res


    def dfshelper(self, candidates, target, index, path, res):
        if target < 0:
            return
        elif target == 0:
            res.append(path)
            return
        for i in range(index, len(candidates)):
            self. dfshelper(candidates, target-candidates[i], i, path+[candidates[i]], res)
