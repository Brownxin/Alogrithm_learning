__author__ = 'Brown'
from functools import reduce

class Solution(object):
    def singleNumber(self, nums):
        xor = reduce(lambda x, y: x ^ y, nums)
        lowbits=xor & -xor
        a,b=0,0
        for num in nums:
            if num & lowbits:
                a^=num
            else:
                b^=num
        return [a,b]