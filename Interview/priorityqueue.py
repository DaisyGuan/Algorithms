from Queue import PriorityQueue

class MyPriorityQueue(PriorityQueue):
    def __init__(self):
        PriorityQueue.__init__(self)
        self.counter = 0

    def put(self, item, priority):
        PriorityQueue.put(self, (priority, self.counter, item))
        self.counter += 1

    def get(self, *args, **kwargs):
        _, _, item = PriorityQueue.get(self, *args, **kwargs)
        return item

#print int(-int('1'))

queue = MyPriorityQueue()
queue.put('item2', 12)
queue.put('item1', -14)

#print queue.get()
queue.put('item3', -12)
#print queue.get()

######################################################
import heapq
from heapdict import heapdict
from Queue import PriorityQueue

h = [5,2,6,8,0,1,2,4]
heapq.heapify(h)#heapify h
print h
heapq.heappush(h,7)#push one into queue
print h
heapq.heappop(h)#pop
print h
heapq.heappushpop(h,3)#pop and push one
print h
heapq.heapreplace(h,6)#pop and replace by one, unsorted
print h

hd = heapdict()
hd[5]=1
hd[3]=2
hd[4]=3
hd.pop
print hd
