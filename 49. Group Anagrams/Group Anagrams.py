class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        res = []
        for char in strs:
            key = ''.join(sorted(char))
            if key not in dic:
                dic[key] = [char]
            else:
                dic[key] = dic[key] + [char]
        for ele in dic:
            res.append(dic[ele])
        return res
