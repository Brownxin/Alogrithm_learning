__author__ = 'Brown'
class Solution(object):
    def isPalindrome(self,s):
        for i in range(len(s)):
            if s[i]!=s[len(s)-1-i]:
                return False
        return True
    def dfs(self,s,list):
        if len(s)==0:
            self.res.append(list)
            return
        for i in range(1,len(s)+1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:],list+[s[:i]])
    def partition(self,s):
        if s==[]:
            return []
        self.res=[]
        self.dfs(s,[])
        return self.res