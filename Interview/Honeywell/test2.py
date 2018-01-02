

class Solution(object):
    def dfs(self, grid,i, j):
        count = 0
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '+':
            return
        grid[i][j] = '#'
        if i == len(grid)-1 and j == len(grid[0])-1:
            count += 1
        return self.dfs(grid, i+1,j) + self.dfs(grid, i, j+1)

matrix = [['+','+'],['+','+']]
print matrix
result = Solution().dfs(matrix, 0, 0)

#can't can't
