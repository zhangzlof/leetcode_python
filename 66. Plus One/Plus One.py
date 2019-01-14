class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        mod = 0
        res = []
        for i in reversed(range(len(digits))):
            mod = (digits[i] + carry) % 10
            carry = (digits[i] + carry) // 10
            res.append(mod)
        if carry == 1:
            res.append(carry)
        return res[::-1]
