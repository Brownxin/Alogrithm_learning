__author__ = 'Brown'
class Solution(object):
    def containsNearbyDuplicate(self,nums,k):
        if nums==[]:
            return False
        dict={}
        for i in range(len(nums)):
            index=dict.get(nums[i])
            if index>=0 and i-index==k:
                return True
            dict[nums[i]]=i
        return False