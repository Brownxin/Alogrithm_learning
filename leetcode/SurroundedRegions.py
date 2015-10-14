__author__ = 'Brown'
class Solution(object):
    def solve(self,board):
        def OtoA(x,y):
            if x>=0 and x<row and y>=0 and y<col and board[x][y]=='O':
                queue.append((x,y))
                board[x][y]='A'
        def bfs(x,y):
            if board[x][y]=='O':
                OtoA(x,y)
            while queue:
                m,n=queue.pop(0)
                OtoA(m-1,n)
                OtoA(m+1,n)
                OtoA(m,n-1)
                OtoA(m,n+1)

        if board==[]:
            return
        row=len(board)
        col=len(board[0])
        queue=[]
        for i in range(row):
            bfs(i,0)
            bfs(i,col-1)
        for i in range(col):
            bfs(0,i)
            bfs(row-1,i)
        for i in range(row):
            for j in range(col):
                if board[i][j]=='A': board[i][j]='O'
                elif board[i][j]=='O': board[i][j]='X'
