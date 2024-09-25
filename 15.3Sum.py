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

nums = [0,1,1]
sol = Solution()
r = sol.threeSum(nums)
print("RESULT: ",r)