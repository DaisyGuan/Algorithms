class Solution(object):
    def findPrevTime(self, time):
        currTime = 60 * int(time[0:2]) + int(time[3:])
        result = currTime
        total = 1440
        temp = []
        for t in time:
            if t != ":":
                temp.append(int(t))

        digitSet = list(set(temp))

        for h1 in digitSet:
            for h2 in digitSet:
                if h1 * 10 + h2 < 24:
                    for m1 in digitSet:
                        for m2 in digitSet:
                            if m1 * 10 + m2 < 60:
                                curr = (h1 * 10 + h2) * 60 + (m1 * 10 + m2)
                                interval = (currTime - curr) % 1440
                                if 0 < interval < total:
                                    result = curr
                                    total = interval


        if result / 60 == 0:
            hour = "00"
        else:
            hour = str(result / 60)

        if result % 60 == 0:
            minute = "00"
        else:
            minute = str(result % 60)

        print hour, minute
        return hour + ":" + minute



newTest = Solution()
newTest.findPrevTime("12:13")
