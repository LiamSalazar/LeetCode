class Solution(object):
    def maxProfit(self, prices):
        minPrice = float('inf')
        earnings = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            if (price - minPrice) > earnings:
                earnings = price - minPrice
        return earnings
prices = [7,1,5,3,6,4]
sol = Solution()
r = sol.maxProfit(prices)
print(r)