__author__ = 'Brown'
from collections import deque
class TreeNode():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution(object):
    def binaryTreePaths(self,root):
        if root==None:
            return []
        res=[]
        queue=deque([[root,str(root.val)]])
        while queue:
            front,path=queue.popleft()
            if front.left==None and front.right==None:
                res.append(path)
                continue
            if front.left:
                queue+=[front.left,path+'->'+str(front.left.val)],
            if front.right:
                queue+=[front.right,path+'->'+str(front.right.val)],
        return res