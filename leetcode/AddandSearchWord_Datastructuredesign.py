__author__ = 'Brown'
class TrieNode:
    def __init__(self):
        self.childs={}
        self.isWord=False

class WordDictionary(object):
    def __init__(self):
        self.root=TrieNode()

    def addWord(self,word):
        node=self.root
        for s in word:
            if not s in node.childs:
                node.childs[s]=TrieNode()
            node=node.childs[s]
        node.isWord=True

    def search(self,word):
        return self.find(self.root,word)

    def find(self,node,word):
        if word=='': return node.isWord
        if word[0]=='.':
            for letter in node.childs:
                if self.find(node.childs[letter],word[1:]):
                    return True
        else:
            child=node.childs.get(word[0])
            if child:
                return self.find(child,word[1:])
        return False