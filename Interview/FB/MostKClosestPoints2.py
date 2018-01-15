"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution(object):
    """
    @param: points: a list of points
    @param: origin: a point
    @param: k: An integer
    @return: the k closest points
    """

    def kClosest(self, points, origin, k):
        def distance(pointa,pointb):
            return abs(pointa[0]-pointb[0])**2 + abs(pointa[1]-pointb[1])**2

        buff_dict = {}
        for point in points:
            #print point
            buff_dict[points.index(point)] = distance(point,origin)
        result = sorted(buff_dict,key = buff_dict.__getitem__)
        res = []
        for r in result[:k]:
            res.append(points[r])
        return res

result = Solution()
#re = result.kClosest([[4,6],[4,7],[4,4],[2,5],[1,1]],[0, 0],3)
redistance = result.kClosest([[4,6],[4,7],[4,4],[2,5],[1,1]],[0, 0],3)
print redistance
