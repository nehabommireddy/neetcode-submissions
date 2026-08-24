class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)

        for i in range (1, len(height)):
            prefix[i] = max(prefix[i-1], height[i-1])
        
        for i in range (len(height)-2, 0, -1):
            suffix[i] = max(suffix[i+1], height[i+1])
            
        
        water = 0
        for i in range (len(height)):
            if (min(prefix[i], suffix[i]) - height[i]) > 0:
                water += min(prefix[i], suffix[i]) - height[i]
        
        return water
