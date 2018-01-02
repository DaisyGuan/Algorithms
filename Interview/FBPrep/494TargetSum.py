class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0

        if nums[0] != 0:
            buff_dict = {nums[0]:1, -nums[0]: 1}
        else:
            buff_dict = {0: 2}

        for i in range(1,len(nums)):
            temp = {}
            for d in buff_dict:
                temp[d+nums[i]] = temp.get(d+nums[i], 0) + buff_dict.get(d, 0)
                temp[d-nums[i]] = temp.get(d-nums[i], 0) + buff_dict.get(d, 0)
            buff_dict = temp
        return buff_dict.get(S, 0)#default is 0
