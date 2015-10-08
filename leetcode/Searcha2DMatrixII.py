__author__ = 'Brown'
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Solution 2
        if matrix==[[]]:
            return False
        def binarySearch(matrix,row,low,high):
            while low<high:
                mid=low+int((high-low)/2)
                if matrix[row][mid]==target:
                    return mid
                elif matrix[row][mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            return high
        col=len(matrix[0])-1
        for i in range(len(matrix)):
            col=binarySearch(matrix,i,)
            if matrix[i][col]==target:
                return True
        return False

        # Solution 1
        # if matrix==[[]]:
        #     return False
        # col=len(matrix[0])-1
        # for row in range(len(matrix)):
        #     while col>-1 and matrix[row][col]>target:
        #         col-=1
        #     if matrix[row][col]==target:
        #         return True
        # return False