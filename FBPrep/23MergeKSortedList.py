#Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""
        :type lists: List[ListNode]
        :rtype: ListNode
        """
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put((node.val,node))

        while q.qsize()>0:
            curr.next = q.get()[1]
            curr=curr.next
            if curr.next:
                q.put((curr.next.val, curr.next))
        return dummy.next
#@kanbumingbai while
#q.put((-n ,n)) for reversed sorted linkedlist
