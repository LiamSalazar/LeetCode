class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged = sorted(nums1 + nums2)
        n = len(merged)
        if n % 2 == 0:
            return (merged[n // 2 - 1] + merged[n // 2])/2.0
        else:
            return merged[n // 2]

nums1 = [1,2]
nums2 = [3,4]
sol = Solution()
r = sol.findMedianSortedArrays(nums1, nums2)
print(r)