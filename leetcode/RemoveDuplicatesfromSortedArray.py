__author__ = 'Brown'
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==None:
            return 0
        p=0
        for i in range(len(nums)):
            if nums[p]!=nums[i]:
                nums[i],nums[p+1]=nums[p+1],nums[i]
                p+=1
        return len(nums[:p+1])
