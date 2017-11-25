class Treenode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Codec(object):
    def serialize(self, root):
        def serial(node):
            if node:
                vals.append(str(node.val))
                serial(node.left)
                serial(node.right)
            else:
                vals.append('#')

        vals = []
        serial(root)
        return ' '.join(vals)#have a blank space here

    def deserialize(self, data):
        def deserial():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = deserial()
            node.right = deserial()
            return node

        vals = iter(data.split())
        return deserial()
