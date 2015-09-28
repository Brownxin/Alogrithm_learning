__author__ = 'Brown'
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # Solution 2
        if matrix==[]:
            return []
        res=[]
        direct=0
        up=0
        left=0
        down=len(matrix)-1
        right=len(matrix[0])-1

        while True:
            if direct==0:
                for i in range(left,right+1):
                    res.append(matrix[up][i])
                up+=1
            if direct==1:
                for i in range(up,down+1):
                    res.append(matrix[i][right])
                right-=1
            if direct==2:
                for i in range(right,left-1,-1):
                    res.append(matrix[down][i])
                down-=1
            if direct==3:
                for i in range(down,up-1,-1):
                    res.append(matrix[i][left])
                left+=1
            if left>right or up>down:
                return res
            direct=(1+direct)%4

        # Solution 1
        # res=[]
        # def dfs(x,y):
        #     if x<0 or y<0 or x>=len(matrix) or y>=len(matrix[0]) or matrix[x][y]=='#':
        #         return
        #     # right
        #     if x==0 or matrix[x-1][y]=='#':
        #         if matrix[x][y]!='#':
        #             res.append(matrix[x][y])
        #         matrix[x][y]='#'
        #         dfs(x,y+1)
        #     # down
        #     if y==len(matrix[0])-1 or matrix[x][y+1]=='#':
        #         if matrix[x][y]!='#':
        #             res.append(matrix[x][y])
        #         matrix[x][y]='#'
        #         dfs(x+1,y)
        #     # left
        #     if x==len(matrix)-1 or matrix[x+1][y]=="#":
        #         if matrix[x][y]!='#':
        #             res.append(matrix[x][y])
        #         matrix[x][y]='#'
        #         dfs(x,y-1)
        #     # up
        #     if x==len(matrix)-1 or matrix[x][y-1]=='#':
        #         if matrix[x][y]!='#':
        #             res.append(matrix[x][y])
        #         matrix[x][y]='#'
        #         dfs(x-1,y)
        # dfs(0,0)
        # return res