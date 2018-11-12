class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        num_str = str(num)
        lg = len(num_str)
        dic3 = {'0':'','1':'C','2':'CC','3':'CCC','4':'CD','5':'D','6':'DC','7':'DCC','8':'DCCC','9':'CM'}
        dic2 = {'0':'','1':'X','2':'XX','3':'XXX','4':'XL','5':'L','6':'LX','7':'LXX','8':'LXXX','9':'XC'}
        dic1 = {'0':'','1':'I','2':'II','3':'III','4':'IV','5':'V','6':'VI','7':'VII','8':'VIII','9':'IX'}
        if (lg == 4):
            result = 'M'*int(num_str[0])
            result = result + dic3[num_str[1]]
            result = result + dic2[num_str[2]]
            result = result + dic1[num_str[3]]
        elif (lg == 3):
            result = dic3[num_str[0]]
            result = result + dic2[num_str[1]]
            result = result + dic1[num_str[2]]
        elif (lg == 2):
            result = dic2[num_str[0]]
            result = result + dic1[num_str[1]]
        else:
            result = dic1[num_str[0]]
        return result




class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = [["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
                 ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
                 ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"], ["", "M", "MM", "MMM"]]
        res = []
        res.append(roman[3][num / 1000 % 10])
        res.append(roman[2][num / 100 % 10])
        res.append(roman[1][num / 10 % 10])
        res.append(roman[0][num % 10])
        return "".join(res)

        
#处理千、百、个位的方法，get，不需要考虑到底是多少位。         
                
            
        
        
