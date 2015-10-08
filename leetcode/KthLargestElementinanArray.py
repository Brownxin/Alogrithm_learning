__author__ = 'Brown'
import random
class Solution(object):
    # Solution 2
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums==[]:
            return None
        num1,num2=[],[]
        tmp=random.choice(nums)
        for num in nums:
            if num>tmp:
                num1.append(num)
            elif num<tmp:
                num2.append(num)
        if len(num1)>=k:
            return self.findKthLargest(num1,k)
        if k>len(nums)-len(num2):
            return self.findKthLargest(num2,k-(len(nums)-len(num2)))
        return tmp

    # Solution 1
    # def getMid(self,list,low,high):
    #     tmp=list[low]
    #     while low<high:
    #         while low<high and list[high]>tmp:
    #             high-=1
    #         if low<high:
    #             list[low]=list[high]
    #             low+=1
    #         while low<high and list[low]<tmp:
    #             low+=1
    #         if low<high:
    #             list[high]=list[low]
    #             high-=1
    #     list[low]=tmp
    #     return low
    # def sort(self,nums,low,high):
    #     if low<high:
    #         mid=self.getMid(nums,low,high)
    #         self.sort(nums,low,mid-1)
    #         self.sort(nums,mid+1,high)
    #
    # def findKthLargest(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: int
    #     """
    #     if nums==[] or len(nums)<k or k<0:
    #         return None
    #     self.sort(nums,0,len(nums)-1)
    #     return nums[len(nums)-k]
