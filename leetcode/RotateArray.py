class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
# Solution 1
        # if nums==None or len(nums)==1:
        #     return nums
        # temp=[]
        # length=len(nums)
        # m=n=(abs(length-k))%length
        #
        # for i in range(len(nums)):
        #     if n>0:
        #         temp.append(nums[i])
        #         n-=1
        #     else:
        #         nums[i-m]=nums[i]
        # index=0
        # for i in range(m,len(nums)):
        #     if index<len(nums):
        #         nums[i]=temp[index]
        #         index+=1
        # return nums

#Solution 2
        n=len(nums)
        nums[:]=nums[n-k:]+nums[0:n-k]
        return nums

