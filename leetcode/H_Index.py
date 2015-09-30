__author__ = 'Brown'
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # Solution 1
        # citations.sort(reverse=True)
        # for i,N in enumerate(citations):
        #     if i>=N:
        #         return i
        # Solution 2
        N=len(citations)
        list=[0]*(N+1)
        for i in citations:
            if i>N:
                list[N]+=1
            else:
                list[i]+=1
        sum=0
        for h in range(N,-1,-1):
            if sum+list[h]>=h:
                return h
            sum+=list[h]
        return 0