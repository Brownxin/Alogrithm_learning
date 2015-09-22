__author__ = 'Brown'
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[len(digits)-1]+=1
        if digits[len(digits)-1]<10:
            return digits
        else:
            for i in range(len(digits)-1,-1,-1):
                if digits[i]>9:
                    digits[i]=0
                    if i-1<0:
                        digits.insert(0,1)
                        break
                    else:
                        digits[i-1]+=1
                else:
                    return digits
        return digits