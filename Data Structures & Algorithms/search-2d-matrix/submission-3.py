class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0

        while i < len(matrix):
            
            if matrix[i][-1] == target:
                return True
            elif matrix[i][-1] < target:
                i += 1
            elif matrix[i][-1] > target:
                break

        if i == len(matrix):
            return False
            
        left, right = 0, len(matrix[i]) - 1
        while left <= right:
            middle = (left + right) // 2
            if matrix[i][middle] == target:
                return True
            elif matrix[i][middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return False