class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums)== 0:
            return []
        if len(nums)== 1:
            return [nums]
        for i in range(len(nums)):
            sub_list = self.permute(nums[:i]+nums[i+1:])  #选出一个数，然后去掉这个数，剩下的数组合，递归
            for j in sub_list:
                res.append([nums[i]]+j)
        return res
