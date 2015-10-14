__author__ = 'Brown'
import collections
class Solution(object):
    def containsNearbyAlmostDuplicate(self,nums,k,t):
        if k<1 or t<0:
            return False
        numDict=collections.OrderedDict()
        for i in range(len(nums)):
            key=nums[i]/max(1,t)
            for m in (key,key-1,key+1):
                if m in numDict and abs(nums[i]-numDict[m])<=t:
                    return True
            numDict[key]=nums[i]
            if i>=k:
                numDict.popitem(0)
        return False