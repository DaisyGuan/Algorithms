class Solution(object):
    def convertToTitle(self, num):
        """
        :type n: int
        :rtype: str
        """
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while num > 0:
            print capitals[(num-1)%26]
            result.append(capitals[(num-1)%26])
            num = (num-1)//26
            print num
        result.reverse()
        return ''.join(result)

result = Solution()
re = result.convertToTitle(28)
print re
