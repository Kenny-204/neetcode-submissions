class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        smap = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if nums[i] in smap:
                return [smap[nums[i]],i]
            else: smap[difference] = i