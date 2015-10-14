__author__ = 'Brown'
class Solution(object):
    def gameOfLife(self,board):
        def getStatus(x,y):
            if x<0 or y<0 or x>len(board)-1 or y>len(board[0])-1:
                return 0
            return board[x][y] & 1
        dx=[-1,-1,-1,0,0,1,1,1]
        dy=[-1,0,1,-1,1,-1,0,1]
        for i in range(len(board)):
            for j in range(len(board[0])):
                lives=0
                for n in range(8):
                    x=i+dx[n]
                    y=j+dy[n]
                    lives+=getStatus(x,y)
                if board[i][j]+lives==3 or lives==3:
                    board[i][j]|=2
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j]>>=1
