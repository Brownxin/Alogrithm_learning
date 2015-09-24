__author__ = 'Brown'
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums==[]:
            return None
        p0=0
        p2=len(nums)-1
        i=0
        while i<=p2:
            if nums[i]==0:
                nums[p0],nums[i]=nums[i],nums[p0]
                p0+=1
                i+=1
            elif nums[i]==2:
                nums[p2],nums[i]=nums[i],nums[p2]
                p2-=1
            else:
                i+=1
        return nums