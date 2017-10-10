def binaryTreeTraversal(root):
        ans, level = [],[root]
        while root and level:
            ans.append([node.val for node in level])
            LRpair = [(node.left, node.right) for node in level]
            level = [leaf for LR in LRpair for leaf in LR if leaf]
        return ans#when from leaf to root[::-1]
