class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        i=0
        j=len(height)-1
        while(i<j):
            max_area = max((j-i)*min(height[i],height[j]),max_area)
            if height[i]<height[j]:
                i = i+1
            else:
                j = j-1
        return max_area
        
