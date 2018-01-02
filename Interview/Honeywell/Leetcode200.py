"""
变形，一个格子周围八个格子都算邻居，用DFS。
"""
class Solution(object):
    def numberofIslands(self, grid):
        if not grid:
            return 0

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return 0

    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i-1, j-1)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i-1, j+1)
        self.dfs(grid, i, j-1)
        self.dfs(grid,i,j+1)
        self.dfs(i+1,j-1)
        self.dfs(i+1,j)
        self.dfs(i+1,j+1)
