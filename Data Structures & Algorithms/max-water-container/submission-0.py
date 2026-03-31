class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            length = min(heights[left], heights[right])
            breadth = right - left
            area = length * breadth

            if area >= max_area:
                max_area = area
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return max_area