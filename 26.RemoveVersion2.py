class Solution(object):
    def removeDuplicates(self, nums):
        j = 1 
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]: 
                nums[j] = nums[i]  
                j += 1  
        return j


# Prueba
sol = Solution()
x = [0,0,1,1,1,2,2,3,3,4]
r = sol.removeDuplicates(x)