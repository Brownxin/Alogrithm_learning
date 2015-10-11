__author__ = 'Brown'
class Solution(object):
    def singleNumber(self,A):
        one=two=three=0
        for i in range(len(A)):
            two|=A[i]&one
            one=one^A[i]
            three=~(one&two)
            one&=three
            two&=three
        return one