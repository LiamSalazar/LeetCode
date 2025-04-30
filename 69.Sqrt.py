class Solution(object):
    def mySqrt(self, x):
        if x == 0:  
            return 0
        
        bottom, top = 0, x
        while bottom <= top:
            r = (top + bottom) // 2
            if r * r == x:  
                return r
            elif r * r < x and (r + 1) * (r + 1) > x:  
                return r
            elif r * r > x:  
                top = r - 1
            else:  
                bottom = r + 1

sol = Solution()
r = sol.mySqrt(12101129000000000000000)
print(r)