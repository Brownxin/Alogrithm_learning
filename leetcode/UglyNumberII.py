__author__ = 'Brown'
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=[1]
        n_2=n_3=n_5=0
        while len(res)<n:
            r_2=res[n_2]*2
            r_3=res[n_3]*3
            r_5=res[n_5]*5
            r=min(r_2,r_3,r_5)
            if r==r_2:
                n_2+=1
            if r==r_3:
                n_3+=1
            if r==r_5:
                n_5+=1
            res+=[r]
        return res[-1]