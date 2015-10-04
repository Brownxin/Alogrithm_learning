__author__ = 'Brown'
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        start=1
        end=1+int((x-1)/2)
        while start<=end:
            center=start+int((end-start)/2)
            if center ** 2==x:
                return center
            elif center ** 2>x:
                end=center-1
            else:
                start=center+1
        return end