class Solution:
    def isMatch(self, s, p):
        i = 0
        j = 0
        start = -1
        sstart = 0
        while i < len(s):
            
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
           
            elif j < len(p) and p[j] == '*':
                start = j
                j += 1
                sstart = i
            
            elif start != -1:
                j = start + 1
                sstart += 1
                i = sstart
      
            else:
                return False
        while j < len(p) and p[j] == '*':
            j += 1
        if j == len(p):
            return True
        return False
