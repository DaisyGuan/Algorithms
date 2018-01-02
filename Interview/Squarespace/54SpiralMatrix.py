class Solution(object):
    def spiralOrder(self, matrix):
        ret = []
        while matrix:
            #right
            ret += matrix.pop(0)
            #print matrix
            #down
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())
            #print matrix
            #left
            if matrix:
                ret += matrix.pop()[::-1]
                #print ret
            #up
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
        return ret


result = Solution().spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])
print result
