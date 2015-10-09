__author__ = 'Brown'
class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BSTiterator(object):
    def __init__(self,root):
        self.stack=[]
        self.pushLeft(root)

    def hasNext(self):
        return self.stack!=[]

    def next(self):
        node=self.stack.pop()
        self.pushLeft(node.right)
        return node.val

    def pushLeft(self,node):
        while node:
            self.stack.append(node)
            node=node.left