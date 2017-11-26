class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        r, c= len(rooms), len(rooms[0])
        for i in xrange(r):
            for j in xrange(c):
                if rooms[i][j] == 0:
                    queue = collections.deque([(i+1, j, 1), (i-1, j, 1), (i, j+1, 1), (i, j-1, 1)])
                    while queue:
                        x, y, val = queue.popleft()
                        if x < 0 or x >= r or y < 0 or y >= c or rooms[x][y] <= val:
                            continue
                        rooms[x][y] = val
                        queue += [(x+1, y, val+1), (x-1, y, val+1), (x, y+1, val+1), (x, y-1, val+1)]#queue.extend([(),(),()])
