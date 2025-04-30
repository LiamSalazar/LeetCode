dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        def dfs(r, c):
            if r >= rows or c >= cols:
                return float('inf')
            if memoize[r][c] != -1:
                return memoize[r][c]
            if r == rows - 1 and c == cols - 1:
                memoize[r][c] = max(1, 1-dungeon[r][c])
                return memoize[r][c]
            memoize[r][c] = max(1, min(dfs(r+1, c), dfs(r, c+1)) - dungeon[r][c])   
            return memoize[r][c]
        rows = len(dungeon)
        cols = len(dungeon[0])
        memoize = [[-1 for _ in range(cols)] for _ in range(rows)]
        return dfs(0,0)
    
sol = Solution()
r = sol.calculateMinimumHP(dungeon)
print(r)