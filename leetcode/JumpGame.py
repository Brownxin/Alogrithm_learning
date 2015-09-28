__author__ = 'Brown'
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<1:
            return True
        cur=0
        p=0
        while p<len(nums)-1:
            cur=max(cur,nums[p])
            if cur==0:
                return False
            p+=1
            cur-=1
        return True