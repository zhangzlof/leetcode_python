class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        dic = {}
        i = 2
        string = '11'
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        
        while(i<n):
            dic[string[0]] = 1
            for j in range(1,len(string)):
                if string[j] not in dic:
                    res = res + str(dic[string[j-1]]) + string[j-1]
                    dic = {}
                    dic[string[j]] = 1
                    if j == len(string)-1 :
                        res=res + '1'+ string[j]
                        dic = {}
                else:
                    dic[string[j]] += 1
                    if j == len(string)-1 :
                        res = res + str(dic[string[j]]) + string[j]
                        dic ={}
            string = res
            res = ''
            i = i + 1
        return string
