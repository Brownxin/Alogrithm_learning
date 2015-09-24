__author__ = 'Brown'
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict={}
        if len(nums)%2==0:
            n=len(nums)/2
        else:
            n=(len(nums)+1)/2
        for i in nums:
            if not i in dict:
                dict[i]=1
            else:
                dict[i]+=1

        for i in dict:
            if dict[i]>=n:
                return i