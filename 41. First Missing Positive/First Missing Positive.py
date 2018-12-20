class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        while(True):
            if i not in nums:
                return i
            else:
                i = i + 1
