__author__ = 'Brown'
class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution(object):
    def postorderTraversal(self,root):
        if root==None:
            return []
        res=[]
        stack=[root]
        previousnode=None
        while stack:
            cur=stack[-1]
            if (previousnode==None) or (previousnode.left==cur) or (previousnode.right==cur):
                if cur.left:
                    stack.append(cur.left)
                elif cur.right:
                    stack.append(cur.right)
            elif previousnode==cur.left and cur.right:
                stack.append(cur.right)
            else:
                res.append(cur.val)
                stack.pop()
            previousnode=cur
        return res