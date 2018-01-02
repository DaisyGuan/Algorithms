import collections
class Solution(object):
    def taskScheduler(self,tasks,N):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        tasks_counts = collections.Counter(tasks).values()
        M = max(tasks_counts)
        Mcount = tasks_counts.count(M)
        return max(len(tasks),(M-1) * (N+1)+ Mcount)


#Idle slots
#ABCD_
#ABC__
#ABC__
#AB

result = Solution()
re = result.taskScheduler(['A','A','B','B','C'],2)
print re

print [1,2,3,4].append([5])
