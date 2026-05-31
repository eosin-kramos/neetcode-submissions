class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maximum = ((right + 1) - (left + 1)) * min(heights[left], heights[right])

        while left < right:
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
            water = ((right + 1) - (left + 1)) * min(heights[left], heights[right]) 
            maximum = max(water, maximum)
        
        return maximum