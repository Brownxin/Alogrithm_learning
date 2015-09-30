__author__ = 'Brown'
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n==0:
            return []
        res=[[0 for i in range(n)] for j in range(n)]
        direct=0
        up=0
        down=n-1
        left=0
        right=n-1
        num=1
        while True:
            if direct==0:
                for i in range(left,right+1):
                    res[up][i]=num
                    num+=1
                up+=1
            elif direct==1:
                for i in range(up,down+1):
                    res[i][right]=num
                    num+=1
                right-=1
            elif direct==2:
                for i in range(right,left-1,-1):
                    res[down][i]=num
                    num+=1
                down-=1
            elif direct==3:
                for i in range(down,up-1,-1):
                    res[i][left]=num
                    num+=1
                left+=1
            # if num>n**2:
            #     return res
            if left>right or up>down:
                return res
            direct=(direct+1)%4