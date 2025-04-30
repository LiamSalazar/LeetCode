class Solution(object):
    def firstMissingPositive(self, nums):
        group = set(nums)
        count = 1
        print(group)
        while True:
            if count in group:
                count +=1
            else:
                return count

# Prueba
nums = [1,2]
sol = Solution()
r = sol.firstMissingPositive(nums)
print(r)  