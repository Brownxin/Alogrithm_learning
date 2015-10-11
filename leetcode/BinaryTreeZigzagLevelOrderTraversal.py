__author__ = 'Brown'
class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution(object):
    def zigzagLevelOrder(self,root):
        if root==None:
            return []
        def preorder(level,node,res):
            if node:
                if level+1>len(res):
                    res.append([])
                if level%2==0:
                    res[level].append(node.val)
                else: res[level].insert(0,node.val)
                preorder(level+1,node.left,res)
                preorder(level+1,node.right,res)

        res=[]
        preorder(0,root,res)
        return res