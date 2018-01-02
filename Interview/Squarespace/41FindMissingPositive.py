[2,3,-1,4,6,0]

[2,3,0,4,0,0]
n=len(nums) = 6

[2,3,6,4,0,0]
[2,3,6,10,0,0]
[8,3,6,10,0,0]
[8,3,6,10,6,0]
[14,3,6,10,6,0]
[20,3,6,10,6,0]


class Solution(object):
    def findMissingPositive(self, nums):
        nums.append(0)
        n = len(nums)

        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for i in range(len(nums)):
            nums[nums[i]%n] += n
        for i in range(len(nums)):
            if nums[i] < n:
                return i

        return n
