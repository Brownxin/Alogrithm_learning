__author__ = 'Brown'
class Solution(object):
    def combine(self,n,k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k==0 or k>n:
            return []
        def dfs(start,list):
            if len(list)==k:
                res.append(list)
                return
            for i in range(start,n+1):
                self.count+=1
                dfs(i+1,list+[i])
                self.count-=1
        res=[]
        self.count=0
        dfs(1,[])
        return res