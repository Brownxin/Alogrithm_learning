__author__ = 'Brown'
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1:
            return 0
        min_price=prices[0]
        max_profit=0
        for i in range(len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            max_profit=max(max_profit,prices[i]-min_price)
        return max_profit