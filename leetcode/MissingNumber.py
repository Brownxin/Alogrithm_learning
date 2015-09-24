__author__ = 'Brown'
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)   # n is the length of nums and n is also the most val of nums
        return (n*(n+1))/2-sum(nums)