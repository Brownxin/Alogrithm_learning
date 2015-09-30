__author__ = 'Brown'
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        mindiff=10**10
        res=0
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while left<right:
                sum=nums[i]+nums[right]+nums[left]
                diff=abs(sum-target)
                if diff<mindiff:
                    mindiff=diff
                    res=sum
                if diff==0:
                    return sum
                elif sum>target:
                    right-=1
                elif sum<target:
                    left+=1
        return res