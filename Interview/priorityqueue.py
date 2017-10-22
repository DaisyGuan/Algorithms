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

print int(-int('1'))

queue = MyPriorityQueue()
queue.put('item2', 12)
queue.put('item1', -14)

#print queue.get()
queue.put('item3', -12)
print queue.get()
