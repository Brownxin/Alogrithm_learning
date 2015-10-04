__author__ = 'Brown'
class Solution(object):
    operation=['+','-','*','/']
    def getVal(self,x,y,operator):
        return {
            '+':lambda x,y : x+y,
            '-':lambda x,y : x-y,
            '*':lambda x,y : x*y,
            '/':lambda x,y : int(float(x/y))
        }[operator](x,y)
    def getPrority(self,operator):
        prority={
            '+':1,
            '-':1,
            '*':2,
            '/':2,
        }
        return prority.get(operator,0)
    def toRPN(self,s):
        number=''
        stackOperator=[]
        token=[]
        for c in s:
            if c.isdigit():
                number+=c
            else:
                if number!='':
                    token.append(number)
                    number=''
                if c in self.operation:
                    while stackOperator!=[] and (self.getPrority(stackOperator[-1])>=self.getPrority(c)):
                        token.append(stackOperator.pop())
                    stackOperator.append(c)
                elif c=='(':
                    stackOperator.append(c)
                elif c==')':
                    while stackOperator!=[] and stackOperator[-1]!='(':
                        token.append(stackOperator.pop())
                    stackOperator.pop()
        if number!='':
            token.append(number)
        while stackOperator!=[]:
            token.append(stackOperator.pop())
        return token
    def evalRPN(self,token):
        res=[]
        for n in token:
            if n.isdigit():
                res.append(int(n))
            else:
                if n in self.operation:
                    y,x=res.pop(),res.pop()
                    res.append(self.getVal(x,y,n))
        return res[0]
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        token=self.toRPN(s)
        return self.evalRPN(token)
