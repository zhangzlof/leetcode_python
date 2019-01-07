class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        for i in range(len(s)-1,-1,-1):
            if s[i] == " ":
                return len(s)-1-i
        return len(s)
