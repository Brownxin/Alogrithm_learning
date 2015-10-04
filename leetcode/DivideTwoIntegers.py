from _testcapi import INT_MIN, INT_MAX

__author__ = 'Brown'
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor==0:
            return None
        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
            if abs(dividend)<abs(divisor):
                return 0
        a=abs(dividend)
        b=abs(divisor)
        count=0
        sum=0
        res=0
        while a>=b:
            sum=b
            count=1
            while sum+sum<=a:
                sum+=sum
                count+=count
            a-=sum
            res+=count
        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
            res=0-res
            return max(res,INT_MIN)
        return min(res,INT_MAX)