class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        total_rain_water = 0
        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]

        while left < right:
            if max_left < max_right:
                left += 1
                max_left = max(height[left], max_left)
                total_rain_water += max_left - height[left]

            else:
                right -= 1
                max_right = max(max_right, height[right])
                total_rain_water += max_right - height[right]
        return total_rain_water

