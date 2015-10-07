__author__ = 'Brown'
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(left,right,list,res):
            if left>right:
                return
            if left==0 and right==0:
                res.append(list)
                return
            if left>0:
                dfs(left-1,right,list+'(',res)
            if right>0:
                dfs(left,right-1,list+')',res)
        res=[]
        dfs(n,n,'',res)
        return res