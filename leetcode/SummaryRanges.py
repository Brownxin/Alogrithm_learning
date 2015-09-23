__author__ = 'Brown'
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if nums==None:
            return None
        if len(nums)==1:
            return [str(nums[0])]
        start=0
        end=0
        res=[]
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>1:
                end=i-1
                if start==end:
                    res.append(str(nums[end]))
                else:
                    res.append(str(nums[start])+'->'+str(nums[end]))
                start=i
                if i==len(nums)-1:
                    res.append(str(nums[start]))
            if i==len(nums)-1 and nums[i]-nums[i-1]==1:
                end=i
                res.append(str(nums[start])+'->'+str(nums[end]))
        return res
