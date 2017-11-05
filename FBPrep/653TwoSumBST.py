class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTarget(self, root, k):
        a = set()
        self.f = False
        def dfs(root, k):
            if not root:
                return self.f
            if root.val not in a:
                a.add(k - root.val)#set has no attribute append, just can use add
            else:
                self.f = True
            dfs(root.left, k)
            dfs(root.right, k)

        dfs(root, k)
        return self.f

node = TreeNode(7)
node.left = TreeNode(8)
node.right = TreeNode(9)

result = Solution()
re = result.findTarget(node,17)
print re
