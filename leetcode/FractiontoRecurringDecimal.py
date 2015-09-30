__author__ = 'Brown'
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        negativeflag=(numerator*denominator<0)
        numlist=[]
        loopdict=dict()
        loopnumber=None
        cnt=0
        numerator=abs(numerator)
        denominator=abs(denominator)

        while True:
            numlist.append(str(int(numerator/denominator)))
            cnt+=1
            numerator=10*(numerator%denominator)
            if numerator==0:
                break
            loc=loopdict.get(numerator)
            if loc:
                loopnumber="".join(numlist[loc:cnt])
                break
            loopdict[numerator]=cnt
        ans=numlist[0]
        if len(numlist)>1:
            ans+="."
        if loopnumber:
            ans+="".join(numlist[1:len(numlist)-len(loopnumber)])+"("+loopnumber+")"
        else:
            ans+="".join(numlist[1:])
        if negativeflag:
            ans="-"+ans
        return ans
