class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        order = []

        while left < right and top < bottom:
            # top fixed, move right
            for c in range(left, right):
                order.append(matrix[top][c])
            
            top += 1

            # right fixed, move down
            for r in range(top, bottom):
                order.append(matrix[r][right -1])
            
            right -= 1

            if not (left < right and top < bottom):
                break
            
            # bottom fixed, move left
            for c in range(right -1, left - 1, -1):
                order.append(matrix[bottom-1][c])
            
            bottom -= 1

            # left fixed, move up

            for r in range(bottom - 1, top-1, -1):
                order.append(matrix[r][left])
            
            left += 1
        
        return order
