__author__ = 'Brown'
import operator
import re

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        operation = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.floordiv
        }

        s = re.sub(r'\d+',' \g<0> ',s)
        expression=s.split()
        total=0
        tmp=0
        index=0
        func=operation['+']
        while index<len(expression):
            e=expression[index]
            if e in '+-':
                total=func(total,tmp)
                func=operation[e]
            elif e in '*/':
                index+=1
                tmp=operation[e](tmp,int(expression[index]))
            else:
                tmp=int(e)
            index+=1
        return func(total,tmp)
