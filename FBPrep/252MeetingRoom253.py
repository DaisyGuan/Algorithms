class Interval(object):
    def __init__(self,s=0,e=0):
        self.start = s
        self.end = e

class Solution(object):
    def canAttendMeetings(self,intervals):
        intervals.sort(key=lamda x:x.start)

        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True
#runningtime O(logn + n)

    def minMeetingRoom(self, intervals):
        startTime = []
        endTime = []

        for interval in intervals:
            startTime.append(interval.start)
            endTime.append(interval.end)

        startTime.sort()
        endTime.sort()
        s = e = 0
        roomCount = len(startTime)

        while s < len(startTime):
            if startTime[s] < endTime[e]:
                s += 1
            else:
                e += 1
                s += 1 #already allocated
                roomCount -= 1

        return roomCount
