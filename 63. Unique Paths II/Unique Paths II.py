class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        res = [[0 for i in range(n)] for i in range(m)]
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                for j in range(i,n):
                    res[0][j] =0
                break
            else:
                res[0][i] = 1
            
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                for j in range(i,m):
                    res[j][0] =0
                break
            else:
                res[i][0] =1

        
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    res[i][j] = 0
                else:
                    res[i][j] = res[i-1][j] + res[i][j-1]
        return res[m-1][n-1]
        
