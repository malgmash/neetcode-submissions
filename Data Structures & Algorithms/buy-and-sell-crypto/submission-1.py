class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        maxdiff = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > maxdiff:
                maxdiff = price - min_price
        return maxdiff