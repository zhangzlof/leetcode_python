class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
    
        lis = []
        for i, row in enumerate(board):
            for j, value in enumerate(row):
                if value != '.':
                    lis += [(value,j),(i,value),(i//3,j//3,value)]
        return len(lis) == len(set(lis))
