class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageLevelBST(self,root):
        info = []
        def dfs(node, depth=0):
            if not node:
                return 0
            if len(info) <= depth:
                info.append([0,0])
            info[depth][0] += node.val
            info[depth][1] += 1
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        dfs(root)
        return [s/float(c) for s, c in info]
