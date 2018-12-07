class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        m = abs(dividend)
        n = abs(divisor)
        res = 0
        if ((dividend >0 and divisor >0) or (dividend <0 and divisor <0)):
            sign = 1
        else:
            sign = -1
        while(m >= n):
            t = n
            i = 1  #record the 2^K
            while(t<<1 < m):
                t = t << 1
                i = i << 1
            m = m - t
            res = res + i
            
        if sign>0 :
            res = res
        else:
            res = -res
        
        if (res>2147483647):
            return 2147483647
        elif (res< -2147483648):
            return -2147483648
        else:
            return res
                
        
