__author__ = 'Brown'
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        max_product=min_product=res=nums[0]
        for i in range(1,len(nums)):
            a=nums[i]*max_product
            b=nums[i]*min_product
            c=nums[i]
            max_product=max(max(a,b),c)
            min_product=min(min(a,b),c)
            res=max(res,max_product)
        return res
