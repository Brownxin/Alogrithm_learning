__author__ = 'Brown'
class Solution(object):
    def compare(self,a,b):
        return [1,-1][a+b>b+a]
    def largestNumber(self,num):
        if num==[]:
            return '0'
        nums=sorted([str(s) for s in num],cmp=self.compare)
        res=''.join(nums).lstrip('0')
        return res or '0'