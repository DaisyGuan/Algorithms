class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = linked_list.head
        while node:
            yield node
            node = node.next

    def add(self, node):
        if self.head:
            self.tail.next = node
        else:
            self.head = node

        self.tail = node

linked_list = SinglyLinkedList()
linked_list.add(Node('Alice'))
linked_list.add(Node('Chad'))
linked_list.add(Node('Debra'))

print [node.value for node in linked_list]  # ['Alice', 'Chad', 'Debra']
#print [node.value for node in llist]


def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1 and l2:
        if l1.val > l2.val:
            l1,l2 = l2, l1

        l1.next = self.mergeTwoLists(l1.next, l2)

    return l1 or l2


#print mergeTwoLists([3,3,3],[1:3,2:4,3:7],[4,5,6])
