class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        j = 1
        while i < len(prices):
            while j < len(prices):
                profit = max(profit, prices[j] - prices[i])
                j += 1
            i += 1
            j = i + 1

        return profit