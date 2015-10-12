__author__ = 'Brown'
class Solution(object):
    def dfs(self,grid,i,j):
        grid[i][j]='0'
        if i>0 and grid[i-1][j]=='1':
            self.dfs(grid,i-1,j)
        if i<len(grid)-1 and grid[i+1][j]=='1':
            self.dfs(grid,i+1,j)
        if j>0 and grid[i][j-1]=='1':
            self.dfs(grid,i,j-1)
        if j<len(grid[0])-1 and grid[i][j+1]=='1':
            self.dfs(grid,i,j+1)

    def numIslands(self,grid):
        if grid==[]:
            return 0
        row=len(grid)
        col=len(grid[0])
        count=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1':
                    count+=1
                    self.dfs(grid,i,j)
        return count