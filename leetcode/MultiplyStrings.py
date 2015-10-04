__author__ = 'Brown'
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1=num1[::-1]
        num2=num2[::-1]
        m=len(num1)
        n=len(num2)
        product=[0 for i in range(m+n)]
        for i in range(m):
            for j in range(n):
                product[i+j]+=int(num1[i])*int(num2[j])
        res=[]
        for k in range(m+n):
            digit=product[k]%10
            carry=int(product[k]/10)
            if k<m+n-1:
                product[k+1]+=carry
            res.insert(0,str(digit))
        while res[0]=='0' and len(res)>1:
            del res[0]
        return ''.join(res)