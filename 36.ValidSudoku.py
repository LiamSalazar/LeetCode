class Solution(object):
    def isValidSudoku(self, board):
        for horizontal in board:
            visited = []
            for vertical in horizontal:
                if vertical != ".":  
                    if vertical in visited:  
                        return False  
                    visited.append(vertical)
        for j in range(9):
            visited = []
            for i in range(9):
                if board[i][j] != ".": 
                    if board[i][j] in visited:  
                        return False  
                    visited.append(board[i][j])
        for box_row in range(0, 9, 3): 
            for box_col in range(0, 9, 3): 
                visited = []
                for i in range(3): 
                    for j in range(3):  
                        value = board[box_row + i][box_col + j]
                        if value != ".":
                            if value in visited:
                                return False
                            visited.append(value)
        return True

board = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
sol = Solution()
print(sol.isValidSudoku(board))