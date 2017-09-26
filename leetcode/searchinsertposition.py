def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        newList = []
        for element in nums:
            if element < target:
                newList.append(element)

        return len(newList)
