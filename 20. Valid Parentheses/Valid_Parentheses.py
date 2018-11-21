class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pars = [ " " ]
        parmap = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in parmap:
                if parmap[c] != pars.pop():
                    return False
            else:
                pars.append(c)
        return len(pars) == 1

        
        
