__author__ = 'Brown'
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Solution 2
        return ' '.join(s.split()[::-1])

        # Solution 1
        # tmp=s.split()
        # res=''
        # for i in range(len(tmp)-1,-1,-1):
        #     res+=' '+tmp[i]
        # return res[1:]