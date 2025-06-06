class Solution(object):
    def minimumTotal(self, triangle):
        if not triangle:
            return 0
        n = len(triangle)
        for i in range(n-2,-1,-1 ):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1])
        return triangle[0][0]