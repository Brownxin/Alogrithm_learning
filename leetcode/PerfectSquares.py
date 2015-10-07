from _testcapi import INT_MAX
import math

__author__ = 'Brown'
class Solution(object):
    _dp=[0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Solution 3
        while n%4==0:
            n/=4
        if n%8==7:
            return 4
        a=0
        while a*a<=n:
            b=int(math.sqrt(n-a*a))
            if a*a+b*b==n:
                if a>0 and b>0:
                    return 2
                elif a>0 or b>0:
                    return 1
            a+=1
        return 3

        # Solution 2
        # dp=self._dp
        # while len(dp)<=n:
        #     dp+=min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1)))+1,
        # return dp[n]

        # Solution 1 --- number theory
        # while n%4==0:
        #     n/=4
        # if n%8==7:
        #     return 4
        # a=0
        # while a*a<=n:
        #     b=math.sqrt(n-a*a)
        #     if a*a+b*b==0:
        #         if a!=0 and b!=0:
        #             return a+b
        # return 3