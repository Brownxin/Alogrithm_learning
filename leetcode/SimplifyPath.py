__author__ = 'Brown'
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # Solution 2
        s=path.split('/')
        res='/'
        for i in s:
            if i=='..':
                if res!='/':
                    res='/'.join(res.split('/')[:-1])
                if res=='': res='/'
            elif i!='.' and i!='':
                if res!='/':
                    res+='/'+i
                else: res+=i
        return res
        # Solution 1
        # if path=='':
        #     return ''
        # res=''
        # stack=[]
        # i=0
        # while i<len(path):
        #     end=i+1
        #     while end<len(path) and path[end]!='/':
        #         end+=1
        #     if i+1<end:
        #         if path[i+1:end]=='..':
        #             if stack!=[]:
        #                 stack.pop()
        #         elif path[i+1:end]!='.':
        #             stack.append(path[i+1:end])
        #     i=end
        #
        # if stack==[]:
        #     return '/'
        # for i in stack:
        #     res+='/'+i
        # return res