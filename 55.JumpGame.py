class Solution(object):
    def canJump(self, nums):
        target = len(nums)-1
        maxI = 0
        if target == 0:
            return True
        for i in range(target):
            if i > maxI:
                return False
            maxI = max(maxI, i + nums[i])
            if maxI >= target:
                return True
        return False