__author__ = 'Brown'
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        sum=0
        valChar={}
        map={'A':0,'C':1,'G':2,'T':3}
        res=[]
        for i in range(len(s)):
            sum=(map[s[i]]+4*sum) & 0xFFFFF

            if i<9: continue
            valChar[sum]=valChar.get(sum,0)+1
            print(sum)
            if valChar[sum]==2:
                res.append(s[i-9:i+1])
        return res