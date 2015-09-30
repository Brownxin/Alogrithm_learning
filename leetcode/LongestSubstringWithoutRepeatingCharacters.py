__author__ = 'Brown'
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        hashtable=[-1 for i in range(256)]
        start=0
        max=0
        for i in range(len(s)):
            if hashtable[ord(s[i])]!=-1:
                while start<=hashtable[ord(s[i])]:
                    hashtable[ord(s[start])]=-1
                    start+=1
            if i-start+1>max: max=i-start+1
            hashtable[ord(s[i])]=i
        return max