class Solution(object):
    def maxArea(self, height):
        r = len(height) - 1
        l = 0
        current = 0
        max_area = 0
        while l < r:
            current = (r - l) * min(height[l], height[r])
            if current > max_area:
                max_area = current
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area

height = [1,8,6,2,5,4,8,3,7]
sol = Solution()
r = sol.maxArea(height)
print("RESULT: ", r)
