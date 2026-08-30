class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        lower = -1

        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                lower = m
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m -1
        
        if lower == -1:
            return [-1,-1]
        
        upper = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                upper = m
                l = m + 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m -1
        
        return [lower, upper]