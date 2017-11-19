class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict1 = {}
        dict1[0] = nums[0]
        for i in range(1,len(nums)):
            dict1[i] = dict1[i-1] * nums[i]
        print dict1
        dict2 = {}
        dict2[len(nums)-1] = nums[len(nums)-1]
        for j in range(len(nums)-2, 0, -1):
            dict2[j] = dict2[j + 1] * nums[j]
        print dict2

        newdict = {}
        newdict[0] = dict2.get(1)
        newdict[len(nums)-1] = dict1.get(len(nums)-2)
        for k in range(1,len(nums)-1):
            newdict[k] = dict1.get(k-1) * dict2.get(k+1)


        return newdict.values()

    def productExceptSelf2(self, nums):
        res = []
        res.append(1)
        for i in range(1, len(nums)):
            res.append(res[i-1] * nums[i-1])
        print res

        temp = 1
        j = len(nums)-1
        while j >= 0:
            res[j] = res[j] * temp
            temp = temp * nums[j]
            j -= 1

        return res


result = Solution()
re = result.productExceptSelf2([1,2,3,4])
print re
