class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = 0   #记录当前位置
        pre = 0   
        count = 0 #记录要跳的步数
        for i in range(len(nums)):
            if i > pre:
                count += 1
                pre = cur
            cur = max(cur,i+nums[i])
        return count
