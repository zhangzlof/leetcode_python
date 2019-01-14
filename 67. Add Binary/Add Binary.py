class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        res = ''
        m = len(a)
        n = len(b)
        if m > n:
            b = '0'*(m-n) + b
        if m < n:
            a = '0'*(n-m) + a
        for i in reversed(range(len(a))):
                mod = ( int(a[i]) + int(b[i]) + carry ) % 2
                carry = ( int(a[i]) + int(b[i]) + carry ) // 2
                res += str(mod)   
        if carry == 1:
            res += str(carry)
        return res[::-1]
