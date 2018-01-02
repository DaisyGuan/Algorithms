#class VersionControl:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use VersionControl.isBadVersion(10) to check whether version 10 is a
# bad version.
class Solution:
    """
    @param n: An integers.
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        if n < 1:
            return -1

        start, end = 1, n
        while start + 1 < end:#if not plus one, infinite loop
            mid = start + (end - start) / 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
        #ordinary case + special case
        if isBadVersion(start):
            return start #for 1 is bad version
        elif isBadVersion(end):
            return end  #for the last good version

        return -1
