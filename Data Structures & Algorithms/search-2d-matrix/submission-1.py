class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        import bisect
        m = len(matrix) - 1
        n = len(matrix[0]) - 1

        high_m = m
        high_n = n
        low_m = 0
        low_n = 0

        while low_m <= high_m:
            middle_m = (low_m + high_m) // 2
            if target <= matrix[middle_m][n] and target >= matrix[middle_m][0]:
                index = bisect.bisect_left(matrix[middle_m], target)
                if index != (n + 1) and matrix[middle_m][index] == target:
                    return True
                else:
                    return False
            elif target < matrix[middle_m][0]:
                high_m = middle_m - 1
            else:
                low_m = middle_m + 1
        return False

