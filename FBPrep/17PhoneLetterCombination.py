class Solution(object):
    def letterCombinations(self,digits):
        mapping = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        result = [""]

        if len(digits) == 0:
            return []

        for digit in digits:
            lst = mapping[digit]
            temp = []
            for i in lst:
                for s in result:
                    temp.append(s+i) #prev is first
            result = temp
        return result

        def letterCombinations2(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        if len(digits) == 0:
            return []

        if len(digits) == 1:
            return list(mapping[digits[0]])

        prev = self.letterCombinations(digits[:-1])
        additional = mapping[digits[-1]]

        return [s + c for s in prev for c in additional]
