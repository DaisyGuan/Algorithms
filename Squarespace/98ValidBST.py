class TreeNode(object):
    def __init__(self,x):
        self.value = x
        self.left = None
        self.right = None

class Solution(object):
    def validBST(self,root,floor=float('-inf'),ceiling=float('inf')):
        if not root:
            return True

        if root.val <= floor or root.val >= ceiling:
            return False

        return self.validBST(root.left, floor, root.val) and self.validBST(root.right, root.val, ceiling)
