class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row
        row_l, row_r = 0, len(matrix) - 1
        def binarySearch(row):
            l, r = 0, len(matrix[row]) - 1
            while l <= r:
                m = l + (r-l)//2
                if matrix[row][m] < target:
                    l = m + 1
                elif matrix[row][m] > target:
                    r = m - 1
                else:
                    return True
            return False

        while row_l <= row_r:
            row = row_l + (row_r - row_l) // 2
            
            if matrix[row][0] > target:
                row_r = row - 1
            elif matrix[row][-1] < target:
                row_l = row + 1
            else:
                return binarySearch(row)
        
        return False
        
        
