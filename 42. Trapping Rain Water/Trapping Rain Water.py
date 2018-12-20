class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0
        res = 0
        max_left, max_right = [0] * len(height), [0] * len(height)
        #记录每个位置的左边最大值
        max_left[0] = height[0]
        for i in range(1,len(height)):
            max_left[i] = max(height[i],max_left[i-1])
        max_right[len(height)-1] = height[len(height)-1]   
        #记录每个位置的右边最大值
        for i in range(len(height)-2,-1,-1):
            max_right[i] = max(height[i],max_right[i+1]) 
            
        for i in range(len(height)):
            res = res + min(max_left[i],max_right[i])-height[i]
            
        return res
