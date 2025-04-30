class Solution(object):
    def maxSubArray(self, nums):
        maxSum = nums[0]  
        currentSum = nums[0] 
        for i in range(1, len(nums)):
            currentSum = max(nums[i], currentSum + nums[i])
            maxSum = max(maxSum, currentSum)
        
        return maxSum
#nums = [-2,1,-3,4,-1,2,1,-5,4]
#nums = [5,4,-1,7,8]
nums = [1]
sol = Solution()
print(sol.maxSubArray(nums))