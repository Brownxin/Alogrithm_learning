__author__ = 'Brown'
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs==['']:
            return [['']]
        dict={}
        res=[]
        for word in strs:
            tmp=''.join(sorted(word))
            if not tmp in dict:
                dict[tmp]=[word]
            else:
                dict[tmp]+=[word]
                dict[tmp].sort()
        for i in dict:
            res.append(dict[i])
        return res