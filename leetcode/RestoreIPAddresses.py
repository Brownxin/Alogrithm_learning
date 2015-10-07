__author__ = 'Brown'
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(s,parts,ip,res):
            if parts==4:
                if s=='':
                    res.append(ip[1:])
                return
            for i in range(1,4):
                if i<=len(s):
                    if int(s[:i])<=255:
                        dfs(s[i:],parts+1,ip+'.'+s[:i],res)
                    if s[0]=='0':
                        break
        res=[]
        dfs(s,0,'',res)
        return res