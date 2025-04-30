class Solution(object):
    def majorityElement(self, nums):
        count = 0
        currentElement = nums[0]
        for num in nums:
            if num == currentElement:
                count += 1
            else:
                count -= 1
            if count < 0:
                currentElement = num
                count = 1
        return currentElement
nums = [3,3,3,2,2,1,1]
sol = Solution()
r = sol.majorityElement(nums)
print(r)