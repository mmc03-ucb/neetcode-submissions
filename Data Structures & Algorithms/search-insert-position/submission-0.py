import bisect
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ix = bisect.bisect(nums, target)
        if ix > 0 and nums[ix - 1] == target:
            return ix - 1
        else:
            return ix