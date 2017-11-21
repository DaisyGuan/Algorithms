class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num:
            A = list(str(num))
            ans = num
            for i in range(len(A)):
                for j in range(i+1, len(A)):
                    A[i], A[j] = A[j], A[i]
                    temp = int(''.join(A))
                    ans = max(ans, temp)
                    A[j], A[i] = A[i], A[j]

            return ans
            
