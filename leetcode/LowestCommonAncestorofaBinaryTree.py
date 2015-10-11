__author__ = 'Brown'
class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution(object):
    def getPath(self,root,node):
        stack=[]
        previous=None
        while stack or root:
            if root:
                stack.append(root)
                root=root.left
            else:
                top=stack[-1]
                if top.right and previous!=top.right:
                    root=top.right
                else:
                    if top==node:
                        return stack
                    previous=stack.pop()
        return stack
    def lowestCommonAncestor(self,root,p,q):
        path_p,path_q=self.getPath(root,p),self.getPath(root,q)
        len_p,len_q=len(path_p),len(path_q)
        x=0
        res=None
        while x<min(len_p,len_q) and path_p[x]==path_q[x]:
            res=path_p[x]
            x+=1
        return res