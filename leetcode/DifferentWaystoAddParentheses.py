__author__ = 'Brown'
import re

class Solution(object):
    def cal(self,a,b,o):
        return {
            '+':lambda x,y: x+y,
            '-':lambda x,y: x-y,
            '*':lambda x,y: x*y
        }[o](a,b)
    def dfs(self,nums,ops):
        if ops==[]:
            return [nums[0]]
        res=[]
        for x in range(len(ops)):
            left=self.dfs(nums[:x+1],ops[:x])
            right=self.dfs(nums[x+1:],ops[x+1:])
            for l in left:
                for r in right:
                    res.append(self.cal(l,r,ops[x]))
        return res

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        nums,ops=[],[]
        s=re.split(r'(\D)',input)
        for i in s:
            if i.isdigit():
                nums.append(int(i))
            else:
                ops.append(i)
        return self.dfs(nums,ops)