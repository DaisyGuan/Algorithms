class Solution(object):
    def search(self, nums, target):
        if not nums:
            return -1

        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)/2
            if (nums[mid]> nums[right] and (target > nums[mid] or target <= nums[right])) or (nums[mid] < target <= nums[right]):
                left = mid + 1
            else:
                right = mid

        if nums[left] == target:
            return left
        else:
            return -1
result = Solution()
re = result.search([4,5,6,7,0,1,2],5)
print re
