__author__ = 'Brown'
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle)==0:
            return 0
        elif len(triangle)==1:
            return triangle[0][0]
        elif len(triangle)==2:
            return min(triangle[1][0],triangle[1][1])+triangle[0][0]
        else:
            res=[]
            for i in range(len(triangle)):
                res.append([0 for j in range(len(triangle[i]))])
            res[0][0]=triangle[0][0]
            for i in range(1,len(triangle)):
                res[i][0]=triangle[i][0]+res[i-1][0]
                res[i][i]=triangle[i][i]+res[i-1][i-1]
            for i in range(2,len(triangle)):
                for j in range(1,i):
                    res[i][j]=triangle[i][j]+min(res[i-1][j],res[i-1][j-1])
            return min(res[len(triangle)-1])