class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreeLevelOrderTraversal(self, root):
        #@type root: TreeNode
        #@type rtype: List[List[int]]
        ans, level = [], [root]
        while root and level:
            # node is not irritable
            ans.append([node.val for node in level])
            LRpair = [(node.left, node.right) for node in level]
            level = [leaf for LR in LRpair for leaf in LR if leaf]
        return ans

class Solution2(object):
    def __init__(self):
        self.l=[]

    def helper(self,root,level):
        if not root:
            return []
        else:
            if level<len(self.l):
                self.l[level].append(root.val)
            else:
                self.l.append([root.val])

            self.helper(root.left,level+1)
            self.helper(root.right,level+1)
        return self.l

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        return self.helper(root,0)
