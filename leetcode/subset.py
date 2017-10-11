def subset(nums):
    res = [[]]
    for num in nums:
        res += [item + [num] for item in res]
    return res


print subset([1,2,3,4])
