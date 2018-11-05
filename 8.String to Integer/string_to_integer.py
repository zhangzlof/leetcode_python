class Solution:
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        temp = s.strip()
        length = len(temp)
        digital_list = ['0','1','2','3','4','5','6','7','8','9']
        if(len(temp)<=1):
            if(temp not in digital_list):
                return 0
            else:
                return int(temp)
        else:
            if temp[0]=='-' or temp[0]=='+':
                result = temp[0]
                for i in range(1,length):
                    if(temp[i] in digital_list):
                        result=result + temp[i]
                    else:
                        break
            elif temp[0] not in digital_list:
                return 0
            else:
                result = ''
                for i in range(length):
                    if(temp[i] in digital_list):
                        result =result + temp[i]
                    else:
                        break
        
        if(result=='-' or result=='' or result=='+'):
            return 0
        elif(int(result)>pow(2,31)-1):
            return pow(2,31)-1
        elif(int(result)<pow(2,31)*(-1)):
            return pow(2,31)*(-1)
        else:
            return int(result)
