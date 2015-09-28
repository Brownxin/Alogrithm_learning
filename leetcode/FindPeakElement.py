__author__ = 'Brown'
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 2
        # if len(nums)==0:
        #     return []
        # if len(nums)==1:
        #     return [0]
        # if len(nums)==2:
        #     if nums[0]>nums[1]: return [0]
        #     if nums[0]<nums[1]: return [1]
        # res=[]
        # low=0
        # high=len(nums)
        # while low<=high:
        #     if low==high:
        #         res.append(low)
        #         break
        #     elif low+1==high:
        #         if nums[0]>nums[1]: res.append(low)
        #         if nums[0]<nums[1]: res.append(high)
        #         break
        #     mid=low+int((high-low)/2)
        #     if nums[mid]<nums[mid-1]:
        #         high=mid-1
        #     elif nums[mid]<nums[mid+1]:
        #         low=mid+1
        #     else:
        #         res.append(mid)
        # return res

        # Solution 1
        res=[]
        def binarySearch(low,high,nums):
            if low==high:
                res.append(low)
                return
            if low+1==high:
                if nums[low]>nums[high]:
                    res.append(low)
                    return
                elif nums[low]<nums[high]:
                    res.append(high)
                    return
            mid=low+int((high-low)/2)
            if nums[mid]<nums[mid-1]:
                binarySearch(low,mid-1,nums)
            if nums[mid]<nums[mid+1]:
                binarySearch(mid+1,high,nums)
        binarySearch(0,len(nums)-1,nums)
        return res