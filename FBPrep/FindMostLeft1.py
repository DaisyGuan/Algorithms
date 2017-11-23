class Solution(object):
    def findMostLeft(self, A):
        """
        rtype:
        """
        i, j = 0, len(A[0])-1
        #pointer = len(A[0])-1
        while 0 <= i < len(A) and 0 <= j < len(A[0]):
            if A[i][j] == 0:
                i += 1
            elif A[i][j]== 1:
                #pointer -= 1
                j -= 1

        return j+1


A =[[0,0,0,1,1],
    [0,0,0,1,1],
    [0,0,0,1,1],
    [0,0,0,1,1],
    [0,0,0,1,1]]
result = Solution().findMostLeft(A)
print result
