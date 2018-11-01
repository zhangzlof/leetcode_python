class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (x==0):
            result=0
        elif (x>0):
            s=str(x)[::-1]         
            for i in range(len(s)):
                if (s[i]!=0):
                    result=int(s[i:])
                    break
        else:
            s=str(x)[1:][::-1]
            for i in range(len(s)):
                if (s[i]!=0):
                    result=int('-'+s[i:])
                    break
            
        if(result<=pow(2,31)-1 and result>=(-1)*pow(2,31)):
            return result
        else:
            return 0
