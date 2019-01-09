class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        Solution.res = 0
        self.dfs(m,n)
        return Solution.res
    def dfs(self, m, n):
        if m==1 and n==1:
            Solution.res += 1
        for i in range(2):
            if i == 0 and m != 1:
                self.dfs(m-1,n)
            if i == 1 and n!= 1:
                self.dfs(m,n-1)


class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        lis = [[0 for i in range(n)] for i in range(m)]
        for i in range(n):
            lis[0][i] = 1
        for j in range(m):
            lis[j][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                lis[i][j] = lis[i-1][j] + lis[i][j-1]
        return lis[m-1][n-1]



