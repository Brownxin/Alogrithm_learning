__author__ = 'Brown'
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        candidates=[i for i in range(1,10)]
        res=[]
        def dfs(candidates,start,target,list):
            if len(list)>k:
                return
            if target==0 and len(list)==k:
                res.append(list)
                return
            for i in range(start,len(candidates)):
                if target<candidates[i]:
                    return
                dfs(candidates,i+1,target-candidates[i],list+[candidates[i]])
        dfs(candidates,0,n,[])
        return res