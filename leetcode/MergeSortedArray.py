__author__ = 'Brown'
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if nums2==None:
            return nums1
        if nums1==None:
            return nums2
        p=m+n-1
        index1=m-1
        index2=n-1
        while index1>-1 and index2>-1:
            if nums1[index1]>nums2[index2]:
                nums1[p]=nums1[index1]
                index1-=1
                p-=1
            else:
                nums1[p]=nums2[index2]
                p-=1
                index2-=1
        if index1>-1:
            for i in range(index1,-1,-1):
                nums1[p]=nums1[i]
                p-=1
        if index2>-1:
            for i in range(index2,-1,-1):
                nums1[p]=nums2[i]
                p-=1
        return nums1