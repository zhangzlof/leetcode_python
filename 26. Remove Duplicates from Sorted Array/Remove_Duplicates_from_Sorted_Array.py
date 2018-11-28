class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        j=0
        for i in range(1,len(nums)):
            if nums[i]!=nums[j]:
                nums[j+1]=nums[i]
                j=j+1
        return  j+1


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        while i<len(nums):
            if nums[i] == nums[i-1]:
                nums.remove(nums[i])
            else:
                i = i + 1
        return len(nums)
            
            
           
            
    
        
