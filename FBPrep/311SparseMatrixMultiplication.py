class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if A is None or B is None:
            return None
        m, n, l = len(A), len(A[0]), len(B[0])
        if len(B) != n:
            return "A's column number must be equal to B's row number."
            #raise Exception("A's column number must be equal to B's row number.")
        C = [[0 for _ in range(l)] for _ in range(m)]
        for i, row in enumerate(A):
            for k, eleA in enumerate(row):
                if eleA:
                    for j, eleB in enumerate(B[k]):
                        if eleB:
                            C[i][j] += eleA * eleB
        return C


result = Solution()
re = result.multiply([[1,2,3],[4,5,6],[7,8,9]],[[100,200,300],[400,500,600],[700,800,900]])
print re
