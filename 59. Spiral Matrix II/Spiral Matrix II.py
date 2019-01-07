class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # 初始化矩阵
        res = [ [0 for i in range(n)] for j in range(n) ]    
        up = 0
        down = n-1
        left = 0
        right = n-1
        step = 0
        key = 1
        while True:
            if step == 0:
                for i in range(left,right+1):
                    res[up][i] = key
                    key = key + 1
                up = up + 1
            if step == 1:
                for i in range(up,down+1):
                    res[i][right] = key
                    key = key + 1
                right = right - 1
            if step == 2:
                for i in range(right,left-1,-1):
                    res[down][i] = key
                    key = key + 1
                down = down - 1
            if step == 3:
                for i in range(down,up-1,-1):
                    res[i][left] = key
                    key = key + 1
                left = left + 1
            if left > right or up > down:
                return res
            step = (step+1) % 4
