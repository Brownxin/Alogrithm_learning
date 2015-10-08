__author__ = 'Brown'
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations==[]:
            return None
        low=0
        high=len(citations)-1
        N=len(citations)
        while low<high:
            mid=low+int((high-low)/2)
            if N-mid>citations[mid]:
                low=mid+1
            else: high=mid-1
        return N-low
