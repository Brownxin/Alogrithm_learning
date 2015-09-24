__author__ = 'Brown'
import math

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # Solution 1
        # depth=0
        # res=[]
        # list=[]
        # while depth<numRows:
        #     for i in range(depth+1):
        #         list.append(math.factorial(depth)/(math.factorial(i)*math.factorial(depth-i)))
        #     res.append(list)
        #     list=[]
        #     depth+=1
        # return res

        # Solution 2
        if numRows==0:
            return []
        if numRows==1:
            return [1]
        if numRows==2:
            return [[1],[1,1]]
        if numRows>2:
            res=[[] for i in range(numRows)]
            for i in range(0,numRows):
                res[i]=[1 for j in range(i+1)]
            for i in range(2,numRows):
                for j in range(1,i):
                    res[i][j]=res[i-1][j-1]+res[i-1][j]
        return res
