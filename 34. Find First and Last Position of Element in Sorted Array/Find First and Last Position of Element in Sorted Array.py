class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums) - 1
        if target not in nums:
            return [-1,-1]
        while (start <= end):
            mid = (start + end)//2
            if (target == nums[mid]):
                start = mid
                end = mid
                while (start-1 >= 0 and target==nums[start-1]):
                    start = start - 1
                while (end+1 <= len(nums)-1 and target == nums[end+1]):
                    end = end + 1
                return [start,end]
            elif (target > nums[mid]):
                start = mid + 1
            else:
                end = mid - 1
