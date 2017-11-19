class Solution(object):
    def dfs(self,island):
        nums = len(island)-1
        if island[0][0] == 1:
            island[0][1], island[1][0] = 0, 0
        if island[nums][nums] == 1:
            island[nums-1][lnums], island[nums][lnums-1] = 0,0
        if island[0][nums] == 1:
            island[1][nums], island[0][nums-1] = 0,0
        if island[nums][0] == 1:
            island[nums-1][0], island[nums][1] = 0,0


        for k in range(1,nums-1):
            if island[0][k] == 1:
                island[0][k-1],island[0][k+1],island[1][k] = 0,0,0
            if island[k][0] == 1:
                island[k-1][0], island[k+1][0],island[k][1] = 0,0,0
            if island[nums][k] == 1:
                island[nums][k-1], island[nums][k+1],island[nums-1][k] = 0,0,0
            if island[k][nums] == 1:
                island[k-1][nums], island[k+1][nums], island[k][nums-1] = 0,0,0

        for i in range(1,len(island)-1):
            for j in range(1,len(island)-1):
                if island[i][j] == 1:
                    if island[i-1][j]:
                        island[i-1][j] = 0
                    if island[i+1][j]:
                        island[i+1][j] = 0
                    if island[i][j-1]:
                        island[i][j-1] = 0
                    if island[i][j+1]:
                        island[i][j+1] = 0
        return island



haha = [[1,0,1,1,0],[1,1,0,1,0],[1,0,0,0,1],[1,1,0,0,0],[0,0,0,0,0]]
result = Solution()
re = result.dfs(haha)
print re

#How to dealing with out of range?
