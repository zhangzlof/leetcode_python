class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def check(k,j):
            for i in range(k):  #check if the kth queen can be put in column j!
                if board[i] == j or (k-i) == abs(board[i] - j):
                    return False
            return True
        def dfs(depth,valuelist):
            if depth == n:
                res.append(valuelist)
                return 
            for i in range(n):
                if check(depth,i):
                    board[depth] = i
                    s = '.'*n
                    dfs(depth+1,valuelist+[s[:i]+'Q'+s[i+1:]])
        res = []
        board = [-1 for i in range(n)]
        dfs(0,[])
        return res
