__author__ = 'Brown'
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Solution 1
        # if len(nums)==0 or nums==None:
        #     return 0
        # length=0
        # for i in range(len(nums)):
        #     if not nums[i]==val:
        #         length+=1
        #
        # return length

        # Solution 2
        end=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==val:
                nums[i],nums[end]=nums[end],nums[i]
                end-=1
        return end+1