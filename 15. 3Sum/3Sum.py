class Solution1:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        lis = []
        for i in range(length):
            for j in range(i+1,length):
                lis1 = []
                if (-nums[i]-nums[j]) in nums[j+1:length]:
                    lis1.append(nums[i])
                    lis1.append(nums[j])
                    lis1.append(-nums[i]-nums[j])
                    
                    if (sorted(lis1) not in lis):
                        lis.append(sorted(lis1))
        return lis




class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solution=[]
        nums.sort()
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                val=nums[i]+nums[left]+nums[right]
                if val==0 and [nums[i],nums[left],nums[right]] not in solution:
                    solution.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                elif val<0:
                    left+=1
                else:
                    right-=1
        return solution



        
        
