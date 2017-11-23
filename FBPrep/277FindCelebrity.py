# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        for cele in range(n):
            temp = range(cele) + range(cele+1, n)
            ind = 0
            while ind < len(temp) and knows(temp[ind], cele) and not knows(cele, temp[ind]):
                ind += 1

            if ind == len(temp):
                return cele
        return -1
            
