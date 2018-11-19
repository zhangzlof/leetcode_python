class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                left = j + 1
                right = len(nums)-1
                
                while(left < right):
                    val = nums[i] + nums[j] + nums[left] + nums[right] - target
                    if (val==0 and [nums[i],nums[j],nums[left],nums[right]] not in result):
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                    elif (val < 0):
                        left += 1
                    else:
                        right -= 1
        return result


        
        
