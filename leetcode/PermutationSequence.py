__author__ = 'Brown'
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # Solution 2
        res=''
        k-=1
        fac=1
        nums=[1,2,3,4,5,6,7,8,9]
        for i in range(1,n):
            fac*=i
        for i in reversed(range(n)):
            cur=nums[k/fac]
            res+=str(cur)
            nums.remove(cur)
            if i!=0:
                k%=fac
                fac/=i
        return res

        # Solution 1 --- TimeLimitExceeded
        # if k==0:
        #     return []
        # res=[]
        # array=[i for i in range(1,n+1)]
        # def dfs(depth,list):
        #     if depth==len(array):
        #         res.append(list)
        #         return
        #     for i in range(0,len(array)):
        #         if not str(array[i]) in list:
        #             dfs(depth+1,list+str(array[i]))
        # dfs(0,'')
        # return res[k-1]