__author__ = 'Brown'
class Solution(object):
    # Solution 2
    def canCompleteCircuit(self,gas,cost):
        if sum(gas)<sum(cost): return -1
        n=len(gas)
        remain=0
        station=0
        for i in range(n):
            if remain+gas[i]<cost[i]:
                station=i+1
                remain=0
            else: remain+=gas[i]-cost[i]
        return station
    # Solution 1-----Time Limited Exceed
    # def canCompleteCircuit(self,gas,cost):
    #     if sum(gas)<sum(cost):
    #         return -1
    #     n=len(gas)
    #     remain=0
    #     station=0
    #     cur=0
    #     while cur<n and station<n:
    #         if remain+gas[cur]<cost[cur]:
    #             station+=1
    #             remain=0
    #             cur=station
    #         else:
    #             remain+=gas[cur]-cost[cur]
    #             cur+=1
    #     return station