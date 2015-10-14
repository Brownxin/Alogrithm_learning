__author__ = 'Brown'
class TrieNode(object):
    def __init__(self):
        self.childs={}
        self.isWord=False
class Trie(object):
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        node=self.root
        for c in word:
            letter=node.childs.get(c)
            if not letter:
                letter=TrieNode()
                node.childs[c]=letter
            node=letter
        node.isWord=True
    def search(self,word):
        node=self.root
        for c in word:
            node=node.childs.get(c)
            if not node:
                return False
        return node.isWord
    def startWith(self,prefix):
        node=self.root
        for c in prefix:
            node=node.childs.get(c)
            if not node:
                return False
        return True