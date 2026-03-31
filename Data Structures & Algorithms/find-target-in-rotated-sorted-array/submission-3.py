class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        res = 0
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] >= nums[0]:
                if target >= nums[0] and nums[middle] > target:
                    right = middle - 1
                else:
                    left = middle + 1
            elif nums[middle] < nums[0]:
                if target <= nums[-1] and nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
        return -1
