class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if matrix == []:
            return []
        up = 0
        down = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        step = 0
        while (True):
            if step == 0:
                for i in range(left,right+1):
                    res.append(matrix[up][i])
                up = up + 1
            if step == 1:
                for i in range(up,down+1):
                    res.append(matrix[i][right])
                right = right - 1
            if step == 2:
                for i in range(right,left-1,-1):
                    res.append(matrix[down][i])
                down = down - 1
            if step == 3:
                for i in range(down,up-1,-1):
                    res.append(matrix[i][left])
                left = left + 1
            if left > right or up > down:
                return res
            step = step + 1
            step = step % 4
        
