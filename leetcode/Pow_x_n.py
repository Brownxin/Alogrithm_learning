__author__ = 'Brown'
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Solution 2
        flag=0
        res=1
        if n==0:
            return 1.0
        if n<0:
            flag=1
            n=-n
        while n>0:
            if n%2==1:
                res=res*x
            x=x*x
            res=x
            n=int(n/2)
        if flag==1:
            return 1.0/res
        return res*1.0

        # Solution 1
        # if n==0:
        #     return 1.0
        # if n<0:
        #     return 1.0/self.myPow(x,-n)
        # if n%2==0:
        #     return self.myPow(x*x,int(n/2))
        # else:
        #     return self.myPow(x*x,int(n/2))*x