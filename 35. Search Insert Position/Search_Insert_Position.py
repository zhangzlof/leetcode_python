class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #方法1
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
    
    
    
        #方法2
        start = 0
        end = len(nums) - 1
        
        while(start <= end):
            mid = (start + end) // 2
            if (nums[mid] == target):
                return mid
            elif (target > nums[mid]):
                start = mid + 1
            else:
                if mid == 0:
                    return 0
                if target > nums[mid-1]:
                    return mid
                else:
                    end = mid -1
        return len(nums)
