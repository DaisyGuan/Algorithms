class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        newcit = sorted(citations, reverse = True)
        res = 0
        for i, j in enumerate(newcit):
            if i < j:
                res += 1
        return res

    def hIndex(self, citations):
        n = len(citations)
        citeCount = [0] * (n+1)
        for c in citations:
            if c >= n:
                citeCount[n] += 1
            else:
                citeCount[c] += 1

        i = n-1
        while i >= 0:
            citeCount[i] += citeCount[i+1]
            if citeCount[i+1] >= i+1:
                return i+1
            i -= 1
        return 0
#The idea is to do binary search to find the min index such that citations[i] >= len(citations) - i,
#then the answer is len(citations)-i
     def hIndex2(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        l, r = 0, n-1
        while l <= r:
            mid = (l+r)/2
            if citations[mid] >= n-mid:
                r = mid - 1
            else:
                l = mid + 1

        return n-l
