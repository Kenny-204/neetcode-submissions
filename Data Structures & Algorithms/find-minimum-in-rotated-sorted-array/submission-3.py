class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        res = nums[0]

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] >= nums[0]:
                left = middle + 1
            else:
                res = nums[middle]
                right = middle - 1

        return res