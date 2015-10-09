__author__ = 'Brown'
class Solution(object):
    def grayCode(self,n):
        if n==0:
            return []
        size=1<<n
        res=[]
        for i in range(size):
            res.append(i^(i>>1))
        return res