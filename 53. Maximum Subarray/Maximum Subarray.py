class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum = cur_sum + nums[i]
            if max_sum < cur_sum:
                max_sum = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        return max_sum
        
