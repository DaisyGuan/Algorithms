class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        ans = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fctn, status, time = log.split(':')
            fctn, time = int(fctn), int(time)

            if status == 'start':
                if stack:
                    ans[stack[-1]] += time - prev_time
                stack.append(fctn)
                prev_time = time
            else:

                ans[stack.pop()] += time - prev_time + 1#stack.pop(), already poped here
                prev_time = time + 1
        return ans


        
