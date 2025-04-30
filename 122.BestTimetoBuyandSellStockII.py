class Solution(object):
    def maxProfit(self, prices):
        earnings = []
        result = 0
        for i in range(len(prices)-1):
            earnings.append(prices[i+1] - prices[i])
        for money in earnings:
            if money > 0:
                result += money
        return result