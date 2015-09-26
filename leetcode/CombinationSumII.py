__author__ = 'Brown'
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res=[]
        def dfs(candidates,start,target,list):
            if target==0 and not list in res:
                res.append(list)
            for i in range(start,len(candidates)):
                if target<candidates[i]:
                    return
                dfs(candidates,i+1,target-candidates[i],list+[candidates[i]])
        dfs(candidates,0,target,[])
        return res