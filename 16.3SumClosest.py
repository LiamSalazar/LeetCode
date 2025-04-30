class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        
        closest = nums[n-1] + nums[n-2] + nums[n-3]
        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            left = i+1
            right = n-1
            while left < right:
                current = nums[i] + nums[left] + nums[right]
                if abs(target - current) < abs(target - closest):
                    closest = current
                if current < target:
                    left += 1
                elif current > target:
                    right -= 1
                else:
                    return current
        return closest
    
nums = [-1,2,1,-4]
target = 1
sol = Solution()
r = sol.threeSumClosest(nums, target)
print("RESULT: ", r)
