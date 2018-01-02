class Solution(object):
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node):
        if not node:
            return None
        if node.label in self.visited:
            return self.visited[node.label]

        clone = UndirectedGraphNode(node.label)
        self.visited[node.label] = clone

        for n in node.neighbors:
            clone.neighbors.append(self.cloneGraph(n))
        return clone
