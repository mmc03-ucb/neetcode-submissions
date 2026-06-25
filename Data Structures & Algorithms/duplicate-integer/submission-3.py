class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsSet = set(nums)
        if len(nums) != len(numsSet):
            return True
        else:
            return False