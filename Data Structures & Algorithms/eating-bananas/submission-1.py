class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxK = max(piles)
        res = float("inf")
        left, right = 1, maxK

        while left <= right:
            middle = (left + right) // 2
            totalHours = 0
            for j in range(len(piles)):
                totalHours += math.ceil(piles[j] / middle)
                if totalHours > h:
                    left = middle + 1
                    break
            if totalHours <= h:
                if middle < res:
                    res = middle
                right = middle - 1
        return res
