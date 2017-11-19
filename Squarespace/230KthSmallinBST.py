#Find second largest in BST
#Find third largest in BST
#Find kth largest in BST
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def firstSmallest(self,root):
        if root.left:
            root = root.left
        else:
            return root.val

    def secondSmallest(self,root):
        if root.left.left:
            root = root.left
        else:
            if not root.left.right:
                return root.val
            else:
                self.firstSmallest(root.left.right)

    def firstLargest(self,root):
        if root.right:
            root = root.right
        else:
            return root.val

    def secondLargest(self,root):
        if root.right.right:
            root = root.right
        else:
            if not root.right.left:
                return root.val
            else:
                self.firstLargest(root.right.left)

    def kthSmallest(root, k):
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

    def kthLargest(root, k):
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.right

            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right


root = TreeNode(7)
root.left = TreeNode(5)
root.left.right = TreeNode(8)
root.right = TreeNode(10)


result = Solution()
re = result.secondLargest(root)
print re
