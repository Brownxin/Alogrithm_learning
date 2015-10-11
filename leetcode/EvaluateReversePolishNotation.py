__author__ = 'Brown'
class Solution(object):
    def calc(self,x,y,o):
        return {
        '+':lambda x,y:x+y,
        '-':lambda x,y:x-y,
        '*':lambda x,y:x*y,
        '/':lambda x,y:-(-x/y) if x*y<0 else x/y
    }[o](x,y)
    operator=['+','-','*','/']
    def evalRPN(self,tokens):
        if tokens==[]:
            return 0
        res=[]
        for n in tokens:
            if not n in self.operator:
                res.append(int(n))
            else:
                if res:
                    y=res.pop()
                    x=res.pop()
                    res.append(self.calc(x,y,n))
        return res[0]
