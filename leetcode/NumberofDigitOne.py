__author__ = 'Brown'
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<0:
            return 0
        one=[0]
        x=0
        while 10**x <= 0x7FFFFFFF:
            one.append(one[x]*10+10 ** x)
            x+=1
        size=len(str(n))-1
        res=0
        for i in str(n):
            digit=int(i)
            n=n-(digit*(10**size))
            if digit==1:
                res+=n+one[size]+1
            elif digit>1:
                res+=digit*one[size]+10**size
            size-=1
        return res