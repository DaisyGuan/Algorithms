class Node(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
#running time: O(logn)
root1 = Node(7)
root1.left = Node(3)
root1.right = Node(2)
root1.left.left = Node(123)
root1.left.right = Node(231)
root1.right.left = Node(9)
root1.right.right = Node(5)


print root1
