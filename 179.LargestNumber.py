class Solution(object):
    def largestNumber(self, nums):
        nums = sorted(nums, key=lambda x: (len(str(x)), -x))
        result = ""
        for num in nums:
            result += str(num)
        return result
    
s = Solution()
print(s.largestNumber([3,30,34,5,9]) )