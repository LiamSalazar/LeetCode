class Solution(object):
    def findPeakElement(self, nums):
        order = sorted(nums)
        num = order[len(nums)]
        return nums.index(num)