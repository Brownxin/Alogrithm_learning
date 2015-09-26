__author__ = 'Brown'
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=2:
            return len(nums)
        p=1
        cur=2
        while cur<len(nums):
            if nums[cur]==nums[p] and nums[cur]==nums[p-1]:
                cur+=1
            else:
                p+=1
                nums[p],nums[cur]=nums[cur],nums[p]
                cur+=1
        return p+1