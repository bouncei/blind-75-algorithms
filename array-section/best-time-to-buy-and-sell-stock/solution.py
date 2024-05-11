class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        lowest_price = prices[0]
        highest_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if price < lowest_price:
                lowest_price = price
                highest_price = price
            elif price > highest_price:
                highest_price = price
                max_profit = max(max_profit, highest_price - lowest_price)

        return max_profit
