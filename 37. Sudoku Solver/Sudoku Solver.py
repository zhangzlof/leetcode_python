class Solution:
    def check(self,x,y,board):
        temp = board[x][y]
        board[x][y] = '.'
        for row in range(9):
            if (board[row][y] == temp):
                return False
        for col in range(9):
            if (board[x][col] == temp):
                return False
        for row in range(3):
            for col in range(3):
                if (board[(x//3)*3+row][(y//3)*3+col]== temp):
                    return False
        board[x][y] = temp
        return True
    def dfs(self,board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for char in '123456789':
                        board[row][col] = char
                        if self.check(row,col,board) and self.dfs(board):
                            return True
                        board[row][col] = '.'
                    return False
        return True
                
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.dfs(board)
