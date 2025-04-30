class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        result = []
        for i in range (n-2):
            for j in range (i+1, n-1):
                for k in range (j+1, n):
                    if(nums[i]+nums[j]+nums[k]==0):
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if(triplet not in result):
                            result.append(triplet)
        return result

nums = [-1, 0, 1, 2, -1, -4]
sol = Solution()
r = sol.threeSum(nums)
print("RESULT: ",r)

# 1 2 3 4 5, n=5
# i j k
# 1 2 3
# 1 2 4
# 1 2 5 
# 1 3 4
# 1 3 5 
# 1 4 5 -
# 2 3 4
# 2 3 5
# 2 4 5 -
# 3 4 5 -
# = n
# = n-1
# for(i=0; j<n-1; i++)