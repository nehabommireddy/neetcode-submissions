class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        rect = {}

        for i in range(len(heights)):
            index1 = i-1
            while index1 >= 0 and heights[index1] >= heights[i]:
                index1 -= 1
            index2 = i+1
            while index2 < len(heights) and heights[index2] >= heights[i]:
                index2 += 1
            rect[i] = [index1, index2]
        
        largest = 0
        for key in rect.keys():
            index1 = rect[key][0]
            index2 = rect[key][1]
            val = heights[key]*(index2-index1-1)
            largest = max(largest, val)
        
        return largest