__author__ = 'Brown'
import math

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res=[0 for i in range(rowIndex+1)]
        for i in range(rowIndex+1):
            res[i]=math.factorial(rowIndex)/(math.factorial(i)*math.factorial(rowIndex-i))
        return res