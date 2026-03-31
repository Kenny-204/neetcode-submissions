class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_map = {}
        length=0
        for num in nums:
            if num not in nums_map:
                nums_map[num] = True
        for num in nums:
            next = num
            temp_length = 1
            while next+1 in nums_map:
                temp_length +=1
                next+=1
            length = max(length,temp_length)
        return length 
            