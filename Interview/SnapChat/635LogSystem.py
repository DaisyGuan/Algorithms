# Time:  put:      O(1)
#        retrieve: O(n + dlogd), n is the size of the total logs
#                              , d is the size of the found logs
# Space: O(n)

class LogSystem(object):

    def __init__(self):
        self.__logs = []
        self.__granularity = {'Year': 4, 'Month': 7, 'Day': 10, \
                              'Hour': 13, 'Minute': 16, 'Second': 19}


    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        self.__logs.append((id, timestamp))


    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        i = self.__granularity[gra]
        begin = s[:i]
        end = e[:i]
        return sorted(id for id, timestamp in self.__logs \
                      if begin <= timestamp[:i] <= end)


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)

"""
You are given several logs that each log contains a unique id and timestamp.
Timestamp is a string that has the following format: Year:Month:Day:Hour:Minute:Second,
for example, 2017:01:01:23:59:59. All domains are zero-padded decimal numbers.

Design a log storage system to implement the following functions:

void Put(int id, string timestamp):
Given a log's unique id and timestamp, store the log in your storage system.

int[] Retrieve(String start, String end, String granularity):
Return the id of logs whose timestamps are within the range from start to end.
Start and end all have the same format as timestamp.
However, granularity means the time level for consideration.
For example, start = "2017:01:01:23:59:59", end = "2017:01:02:23:59:59",
granularity = "Day", it means that we need to find the logs within the range from Jan. 1st 2017 to Jan. 2nd 2017.
