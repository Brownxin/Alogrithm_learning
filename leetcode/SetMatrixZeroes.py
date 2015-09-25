__author__ = 'Brown'
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row_length=len(matrix)
        col_length=len(matrix[0])
        row=[False for i in range(row_length)]
        col=[False for i in range(col_length)]

        for i in range(row_length):
            for j in range(col_length):
                if matrix[i][j]==0:
                    row[i]=True
                    col[j]=True
        for i in range(row_length):
            for j in range(col_length):
                if row[i] or col[j]:
                    matrix[i][j]=0
        return matrix