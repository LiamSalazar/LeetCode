class Solution(object):
    def twoSum(self, nums, target):
        for i in range (len(nums)):
            left = target - nums[i]
            if left in nums[i+1:]:
                return [i,nums.index(left, i+1)]

        
nums = [3,2,3]
# 32 34 35 36
# 24 25 26
# 45 46
# 56
target = 6
sol = Solution()
r = sol.twoSum(nums, target)
print(r)