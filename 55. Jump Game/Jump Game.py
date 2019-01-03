class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cur_pos = 0
        if len(nums)== 1:
            return True
        if nums == []:
            return True
        for i in range(len(nums)):
            if i == cur_pos:
                if nums[i] == 0:             #当走到最大位置处，并且刚好该位置值为0，则无法通过该位置，到达不了终点
                    return False
            cur_pos = max(cur_pos,nums[i]+i)    #保存最大的位置
            if cur_pos >= len(nums)-1:
                return True
