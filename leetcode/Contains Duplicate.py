__author__ = 'Brown'
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict={}
        for i in range(len(nums)):
            if not nums[i] in dict:
                dict[nums[i]]=1
            else:
                dict[nums[i]]+=1
                return True
        return False