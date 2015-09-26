__author__ = 'Brown'
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        candidates.sort()
        def dfs(target,start,candiates,list):
            if target==0:
                res.append(list)
                return
            for i in range(start,len(candidates)):
                if target<candidates[i]:
                    return
                dfs(target-candidates[i],i,candidates,list+[candidates[i]])
        dfs(target,0,candidates,[])
        return res