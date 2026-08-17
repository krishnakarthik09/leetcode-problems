class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        mini=prices[0]
        for i in range(1,len(prices)):
            pro=prices[i]-mini
            profit=max(profit,pro)
            mini=min(mini,prices[i])
        return profit
        