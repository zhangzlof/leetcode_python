class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic ={"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],
              "6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return [element for element in dic[digits]]
        else:
            for i in range(1,len(digits)):
                lis = []
                for cha in dic[digits[0:i]]:
                    for element in dic[digits[i]]:
                        lis.append(cha+element)
                dic[digits[0:i+1]] = lis
            return lis


        
        
