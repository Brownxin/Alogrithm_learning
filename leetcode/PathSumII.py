__author__ = 'Brown'
class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution(object):
    def pathSum(self,root,sum):
        def dfs(root,cursum,list):
            if root.left==None and root.right==None:
                if cursum==sum:
                    res.append(list)
                return
            if root.left:
                dfs(root.left,cursum+root.left.val,list+[root.left.val])
            if root.right:
                dfs(root.right,cursum+root.right.val,list+[root.right.val])

        if root==None:
            return []
        res=[]
        dfs(root,root.val,[root.val])
        return res