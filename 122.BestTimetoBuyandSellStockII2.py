class Solution(object):
    def maxProfit(self, prices):
        result = 0
        for i in range(len(prices)-1):
            if (prices[i+1] - prices[i]) > 0:
                result += prices[i+1] - prices[i]
        return result
    
sol = Solution()
print(sol.maxProfit([2,4,1]))
print(sol.maxProfit([3,2,6,5,0,3]))