class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            
            for i in range(left, right):
                res.append(matrix[top][i])
                print(f"top: {top}")
                # print(f"")
            top += 1

            for i in range(top, bottom):
                print(right)
                res.append(matrix[i][right - 1])
            right -= 1

            if not (top < bottom and left < right):
                break
            
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        
        return res