class Solution(object):
    def trap(self, height):
        n = len(height)
        leftWall, rightWall = 0
        maxRight = [0] * n
        maxLeft = [0] * n
        sum = 0
        for i in range(n):
            j = -i-1
            maxLeft[i] = leftWall
            maxRight[j] = rightWall
            leftWall = max(leftWall, height[i])
            rightWall = max(rightWall, height[j])
        for i in range(n):
            pot = min(maxLeft[i], maxRight[i])
            sum += max(0, pot - height[i])
        return sum