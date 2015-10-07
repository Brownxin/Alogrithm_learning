__author__ = 'Brown'
class Solution(object):
    # Solution 2
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits=='':
            return []
        dict={
                '2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']
            }

        def dfs(curr,digit,res):
            if curr==length:
                res.append(digit)
                return
            for i in dict[digits[curr]]:
                dfs(curr+1,digit+i,res)

        res=[]
        length=len(digits)
        dfs(0,'',res)
        return res
    # Solution 1
    # dict={
    #     '2':['a','b','c'],
    #     '3':['d','e','f'],
    #     '4':['g','h','i'],
    #     '5':['j','k','l'],
    #     '6':['m','n','o'],
    #     '7':['p','q','r','s'],
    #     '8':['t','u','v'],
    #     '9':['w','x','y','z']
    # }
    # def dfs(self,curr,digit,digits):
    #     if curr==len(digits):
    #         self.res.append(digit)
    #         return
    #     for i in self.dict[digits[curr]]:
    #         self.dfs(curr+1,digit+i,digits)
    # def letterCombinations(self, digits):
    #     """
    #     :type digits: str
    #     :rtype: List[str]
    #     """
    #     if digits=='':
    #         return []
    #     self.res=[]
    #     self.dfs(0,'',digits)
    #     return self.res