# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max = 0
        min = prices[0]

        for n in prices:
            if n - min > max:
                max = n - min
            if n < min:
                min = n

        return max
