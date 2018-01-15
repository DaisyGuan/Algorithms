class Solution(object):

    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.lt = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        newlist = []
        for i in range(len(self.lt)):
            if self.lt[i] == target:
                newlist.append(i)

        return random.choice(newlist)



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)a
