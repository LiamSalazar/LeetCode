class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
        return l


nums = [1,3,5,6]
target = 5
sol = Solution()
r = sol.searchInsert(nums, target)
print("RESULT: ", r)
