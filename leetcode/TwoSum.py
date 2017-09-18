
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if len(nums) <= 1:
        return False
    buff_dict = {}
    for i in range(len(nums)):
        if nums[i] in buff_dict:
            return [buff_dict[nums[i]],i]
        else:
            buff_dict[target-nums[i]] = i
            #print buff_dict


#print twoSum([1,5,3],8)
