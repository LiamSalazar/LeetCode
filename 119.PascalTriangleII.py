class Solution(object):
    def getRow(self, rowIndex):
        numRows = rowIndex + 1
        result = []
        if numRows == 1:
            return [1]
        if numRows == 2:
            return [1,1]
        result += [[1], [1, 1]]
        for i in range(2, numRows):
            temporal = []
            for j in range(i+1):
                if j == 0 or j == i:
                    temporal.append(1)
                else:
                    temporal.append(result[i-1][j-1] + result[i-1][j])
            result.append(temporal)
        return result[rowIndex]
sol = Solution()
r = sol.generate(5)
print(r)