class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        Solution.temp = 0
        Solution.res = ""
        lis = [i for i in range(1,n+1)]
        self.dfs(lis,"",k)
        return Solution.res
            
    def dfs(self,lis,char,k):
        if lis == []:
            Solution.temp += 1
            if Solution.temp == k:
                Solution.res = char
                return
        for i in range(len(lis)):
            self.dfs(lis[0:i] + lis[i+1:],char + str(lis[i]),k)




class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ''
        k = k - 1
        fac = 1
        for i in range(1,n):
            fac = fac*i
        num = [i for i in range(1,n+1)]
        for i in reversed(range(n)):
            cur = num[k//fac]
            res = res + str(cur)
            num.remove(cur)
            if i != 0:
                k = k%fac
                fac = fac//i
        return res
