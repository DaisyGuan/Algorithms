# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        #check whether match or not
    def isMatch(self, s, t):
        if not(s and t):
            return s is t #is is the identity comparison；== is the equality comparison.
        return (s.val == t.val and self.isMatch(s.left, t.left) and self.isMatch(s.right, t.right))

    def isSubtree(self, s, t):
        if self.isMatch(s, t):
            return True
        if not s: # if s disappear
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
#For each node of s, let's check if it's subtree equals t. 
