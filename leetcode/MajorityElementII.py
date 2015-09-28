__author__ = 'Brown'
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==0:
            return []
        dict={}
        res=[]
        if len(nums)%3==0:
            n=len(nums)/3
        else:
            n=int(len(nums)/3)
        for num in nums:
            if not num in dict:
                dict[num]=1
            else: dict[num]+=1
        for i in dict:
            if dict[i]>n:
                res.append(i)
        return res