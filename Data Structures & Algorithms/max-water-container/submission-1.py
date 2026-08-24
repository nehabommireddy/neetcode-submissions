class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxi = 0

        while left < right:
            amt = min(heights[left],heights[right]) * (right - left)
            maxi = max (amt, maxi)
            if heights[left] <= heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
        
        return maxi