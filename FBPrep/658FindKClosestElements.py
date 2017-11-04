#Given a sorted array, two integers k and x,
#find the k closest elements to x in the array.
#The result should also be sorted in ascending order. 
#If there is a tie, the smaller elements are always preferred.
class Solution(object):
     def findClosestElements(self, arr, k, x):
        end = k
        arr.sort()
        print arr
        for i in range(k, len(arr)):
            delta = abs(arr[i] - x) - abs(arr[i - k] - x)
            if delta > 0:
                return arr[end - k:end]
            if delta < 0:
                end = i + 1
        return arr[end - k:end]

#running time O(logn + n)
#priorityqueue running time O(logn)
result = Solution()
re = result.findClosestElements([1,5,6,2,73],2,2)
print re
