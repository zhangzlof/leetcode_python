class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        numsLen = len(nums)
        var = numsLen - 1
        for i in range(numsLen-1,-1,-1):
            if nums[i] > nums[i-1]:
                var = i-1  #find the value
                break
        if var == numsLen - 1:
            nums.reverse()
        else:
            for j in range(numsLen-1,-1,-1):
                if nums[j] > nums[var]:
                    temp = nums[var]
                    nums[var] = nums[j]
                    nums[j] = temp
                    break
            nums[var+1:] = sorted(nums[var+1:])
        
