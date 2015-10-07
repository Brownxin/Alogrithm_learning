__author__ = 'Brown'
class Solution(object):
    def getLongestPalindrome(self,s,l,h):
        while l>=0 and h<len(s) and s[l]==s[h]:
            l-=1; h+=1
        return s[l+1:h]
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_palindrome=''
        for i in range(len(s)):
            len1=self.getLongestPalindrome(s,i,i)
            len2=self.getLongestPalindrome(s,i,i+1)
            if len(len1)>len(len2):
                if len(len1)>len(max_palindrome):
                    max_palindrome=len1
            else:
                if len(len2)>len(max_palindrome):
                    max_palindrome=len2
        return max_palindrome