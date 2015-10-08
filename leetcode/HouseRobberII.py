__author__ = 'Brown'
class Solution(object):
    def totalValue(self,nums):
        odd=even=0
        for i in range(len(nums)):
            if i%2==0:
                even=max(odd,even+nums[i])
            else: odd=max(even,odd+nums[i])
        return max(odd,even)
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:
            return 0
        if len(nums)==1:
            return nums[0]
        return max(self.totalValue(nums[1:]),self.totalValue(nums[:len(nums)-1]))