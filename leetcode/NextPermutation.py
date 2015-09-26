__author__ = 'Brown'
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)<2:
            return nums
        p=-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                p=i
                break
        if p==-1:
            nums.reverse()
            return nums
        else:
            for i in range(len(nums)-1,p,-1):
                if nums[i]>nums[p]:
                    nums[i],nums[p]=nums[p],nums[i]
                    break
            left=p+1
            right=len(nums)-1
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
            return nums