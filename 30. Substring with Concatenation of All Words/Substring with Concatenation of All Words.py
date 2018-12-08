class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if words == []:
            return []
        dic1 = {}
        for word in words:
            if word not in dic1:
                dic1[word] = 1
            else:
                dic1[word] += 1
        wl = len(words)
        sl = len(s)
        wordl = len(words[0])
        sub_sl = wl*wordl
        res = []
        for i in range(0,sl-sub_sl+1):
            curr={}
            j=0
            while j<wl:
                word=s[i+j*wordl:i+j*wordl+wordl]
                if word not in words: 
                    break
                if word not in curr: 
                    curr[word]=1
                else:
                    curr[word]+=1
                if curr[word]>dic1[word]: 
                    break
                j+=1
            if j==wl:
                res.append(i)
        return res
