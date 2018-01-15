class Solution1(object):
    def find1stsmall(self,A):
        return sorted(A)[0]

    def find2ndsmall(self,A):
        return sorted(A)[1]

    def findkthsmall(self,A,k):
        return sorted(A)[k-1]

class Solution2(object):
    def find1stsmall(self,A):
        minEle = A[0]
        for i in range(len(A)):
            minEle = min(minEle, A[i])
        return minEle

    def find2ndsmall(self,nums):
        if len(nums) > 2:
            big, small = max(nums[0],nums[1]), min(nums[0],nums[1])
            for k in range(2, len(nums)):
                if small <= nums[k] < big:
                    big = nums[k]
                elif nums[k] < small:
                    big = small
                    small = nums[k]
            return big
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            return False

    def findkthsmall(self,A,k):
        return sorted(A)[k-1]





result2 = Solution2()
re1 = result2.find1stsmall([1,4,2])
print re1
re2 = result2.find2ndsmall([1,4,2])
print re2
re3 = result2.findkthsmall([1,4,2],3)
print re3
