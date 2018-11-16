class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest_sum = sys.maxsize
        for i in range(len(nums)-2): 
            if i == 0 or nums[i] > nums[i-1]:     #排除相同的数
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    diff = nums[left] + nums[right] + nums[i] - target
                    if abs(diff) < abs(closest_sum):
                        closest_sum = diff
                    if diff == 0:
                        return target
                    elif diff < 0:
                        left += 1
                    else:
                        right -= 1

        return closest_sum + target  



        
        
