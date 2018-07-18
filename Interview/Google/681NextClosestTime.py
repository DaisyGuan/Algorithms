class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """

        digitSet = list(set(time[:2] + time[3:]))
        digitSet.sort()

        big = str(max(digitSet))
        small = str(min(digitSet))
        if len(digitSet) == 1:
            return time

        if time[-1] != max(digitSet):
            return str(time[:4] + big)
        elif time[-2] != max(digitSet):
            temp1 = digitSet.indexof(time[-2]) + 1
            if digitSet(temp1) <= 5:
                return str(time[:3] + sml1+ small)
            else

            while digitSet(temp1) > 5 and temp1 <= len(digitSet):
                temp1 += 1
            

        elif time[1] != max(digitSet):
            temp2 = digitSet.indexof(time[1]) + 1
            sml2 = digitSet[temp2]
            return str(time[:1] + sml2 + ":" + small + small)
        elif time[0] != max(digitSet):
            temp3 = digitSet.indexof(time[0]) + 1
            sml3 = digitSet[temp3]
            return sml3 + small + ":" + small + small
        else:
            if

        print max(digitSet)

    #def dfsHelper(self, res, idx, path):



newTest = Solution()
newTest.nextClosestTime("18:19")
