class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r  = 1
        profit = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                new_price = prices[r] - prices[l]
                profit = max(profit, new_price)
            else:
                l=r
            r+=1
        return profit
