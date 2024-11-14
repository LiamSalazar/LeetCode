class Solution(object):
    def rotate(self, matrix):
        max = len(matrix)
        for i in range(max):
            for j in range(i, max):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(max):
            matrix[i].reverse()
        return matrix

# 0 1 2
# 3 4 5
# 6 7 8

# 6 3 0
# 7 4 1
# 8 5 2

#  i j   i j   i j
# (0,0) (0,1) (0,2)
# (1,0) (1,1) (1,2)
# (2,0) (2,1) (2,2)

#  j i   j i   j i
# (2,0) (1,0) (0,0) 
# (2,1) (1,1) (0,1)
# (2,2) (1,2) (0,2) 

sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
r = sol.rotate(matrix)
print (r)