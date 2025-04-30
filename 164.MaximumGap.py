class Solution(object):
    def maximumGap(self, nums):
        max = 0
        nums.sort()
        for i in range(1, len(nums)):
            if abs(nums[i] - nums[i - 1]) >= max:
                max = abs(nums[i] - nums[i - 1])
        return max