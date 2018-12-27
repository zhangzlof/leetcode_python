class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)== 0:
            return []
        if len(nums)== 1:
            return [nums]
        res = []
        pre = None
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == pre:
                continue
            pre = nums[i]
            sublist=self.permuteUnique(nums[:i] + nums[i+1:])
            for j in sublist:
                res.append([nums[i]]+j)
        return res
