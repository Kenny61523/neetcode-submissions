
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False  # Edge case: empty matrix
        
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1  # Treat as a 1D array

        while left <= right:
            mid = left + (right - left) // 2
            r, c = mid // cols, mid % cols  # Convert 1D index to 2D

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False  # Target not found
        
        


