class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])

        order = []

        while left < right and top < bottom:
            for c in range(left, right):
                order.append(matrix[top][c])
            
            top += 1

            for r in range(top, bottom):
                order.append(matrix[r][right - 1])
            
            right -= 1

            if not (top < bottom and left < right):
                break
            
            for c in range(right - 1, left - 1, -1):
                order.append(matrix[bottom - 1][c])
            
            bottom -= 1

            for r in range(bottom - 1, top -1, -1):
                order.append(matrix[r][left])
            
            left += 1
        
        return order