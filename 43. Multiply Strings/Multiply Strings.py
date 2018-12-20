class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = []
        bit_sum = [0 for i in range(len(num1)+len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                bit_sum[i+j] += int(num1[i])*int(num2[j])
                
        for i in range(len(bit_sum)):
            digital = bit_sum[i] % 10
            carry = bit_sum[i] // 10
            if i < len(bit_sum) - 1:
                bit_sum[i+1] += carry
            res.insert(0,str(digital))
        while res[0] == '0' and len(res)>1 :
            del res[0]
        return ''.join(res)
