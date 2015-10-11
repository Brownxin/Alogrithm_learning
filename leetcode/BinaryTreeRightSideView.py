__author__ = 'Brown'
class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution(object):
    def rightSideView(self,root):
        if root==None:
            return None
        res=[]
        queue=[root]
        while queue:
            size=len(queue)
            for r in range(size):
                root=queue.pop(0)
                if r==0:
                    res.append(root.val)
                if root.right:
                    queue.append(root.right)
                if root.left:
                    queue.append(root.left)
        return res