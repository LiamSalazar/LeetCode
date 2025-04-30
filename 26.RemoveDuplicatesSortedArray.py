class Solution(object):
    def removeDuplicates(self, nums):
        visited = []
        j = 0
        for i in range(len(nums)):
            if nums[i] not in visited:
                visited.append(nums[i])
                nums[j] = nums[i]
                j+=1
        return j

# Prueba
sol = Solution()
x = [0,0,1,1,1,2,2,3,3,4]
r = sol.removeDuplicates(x)