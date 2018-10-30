class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length=len(s)
        res=""
        if(length==0 or numRows==1):
            return s
        for i in range(0,numRows):
            if(i<length):
                indx = i
                res += s[indx]
                k=1
                
            while(indx < length):
                if(i==0 or i==numRows-1):
                    indx += 2 * numRows - 2
                else:
                    if(k%2==1):
                        indx += 2 * (numRows - 1 - i)
                    else:
                        indx += 2 * i
                if (indx < length):
                    res += s[indx]
                k=k+1
        return res