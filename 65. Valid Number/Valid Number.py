class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        num = False
        dot = False
        exp = False
        for i in range(len(s)):
            if s[i] >= '0' and s[i] <= '9':
                num = True
            elif s[i] == '.':
                if dot or exp:
                    return False
                dot = True
            elif s[i] == 'e':
                if exp or not num:
                    return False
                exp =True
                num =False
            elif s[i] == '+' or s[i] == '-':
                if i!=0 and s[i-1] != 'e':
                    return False
            else:
                return False
        return num
            
