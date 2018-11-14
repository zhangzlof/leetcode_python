class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        num = len(strs)
        
        if num == 0:
            return ""
        elif num== 1:
            return strs[0]
        else:
            if ("" in strs):
                return ""
            min_length = len(strs[0])
            for element in strs:
                if (len(element)<min_length):
                    min_length = len(element)
            
            a = 0
            for i in range(min_length):
                for j in range(1,num):
                    if (strs[j][i] == strs[0][i]):
                        if (j == num-1):
                            a = a + 1
                    else:
                        return strs[0][0:a]
            return strs[0][0:a]
            
        
        
