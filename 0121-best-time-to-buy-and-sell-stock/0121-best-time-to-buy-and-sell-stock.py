class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left=0
        right=1
        maxprofit=0
        while right<len(prices):
            if prices[right]>prices[left]:
                profit=prices[right]-prices[left]
                maxprofit=max(maxprofit, profit)
            else:
                left=right
            right+=1
        return maxprofit