class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums, reverse=True)[k-1]
#running time O(nlogn) because the build-in function
x = Solution()
print x.findKthLargest([2],1)

    #bubble sort
    def findKthLargest2(self,nums,k):
        for i in range(k):#choose most k, ignore about k-1 situation in bubblesort #have most k listed at end of the list
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums[len(nums)-k]

"""
range creates a list, so if you do range(1, 10000000) it creates a list in memory with 9999999 elements.

xrange is a sequence object that evaluates lazily.
"""
