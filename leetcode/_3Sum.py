__author__ = 'Brown'
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Solution 1
        if nums==None or len(nums)<3:
            return []
        nums.sort()
        dict={}
        res=[]
        for i in range(len(nums)):
            dict[-nums[i]]=i
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                target=nums[i]+nums[j]
                if target in dict:
                    if dict[target]>j:
                        if not [nums[i],nums[j],nums[dict[target]]] in res:
                            res.append([nums[i],nums[j],nums[dict[target]]])
        return res

        # Solution 2
        # num.sort()
        # res = []
        # for i in range(len(num)-2):
        #     if i == 0 or num[i] > num[i-1]:
        #         left = i + 1; right = len(num) - 1
        #         while left < right:
        #             if num[left] + num[right] == -num[i]:
        #                 res.append([num[i], num[left], num[right]])
        #                 left += 1; right -= 1
        #                 while left < right and num[left] == num[left-1]: left +=1
        #                 while left < right and num[right] == num[right+1]: right -= 1
        #             elif num[left] + num[right] < -num[i]:
        #                 while left < right:
        #                     left += 1
        #                     if num[left] > num[left-1]: break
        #             else:
        #                 while left < right:
        #                     right -= 1
        #                     if num[right] < num[right+1]: break
        # return res