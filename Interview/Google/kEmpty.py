class Solution(object):
    def solution(self, A, K, M) :
        l = len(A)
        latest = -2
        root = [-1] * l
        length = [0] * l
        count = 0
        for i in xrange(l):
            curr = A[i] - 1
            root[curr] = curr
            length[curr] = 1
            if curr + 1 < l and root[curr + 1] > -1:
                if length[curr + 1] >= K:
                    count -= 1
                root[curr + 1] = curr
                length[curr] += length[curr + 1]
            if curr - 1 > -1 and root[curr - 1] > -1:
                root[curr] = self.findRoot(root, curr - 1)
                length[root[curr]] += length[curr]
                if length[root[curr]] >= K and length[root[curr]] - length[curr] < K:
                    count += 1
            elif length[curr] >= K:
                count += 1
            if count == M: latest = i
        return latest + 1

    def findRoot(self, root, n):
        while root[n] != n:
            root[n] = root[root[n]]
            n = root[n]

        return n

A = [1,4,3,2,5]
K = 1
M = 3
a = Solution()
print a.solution(A, K, M)
