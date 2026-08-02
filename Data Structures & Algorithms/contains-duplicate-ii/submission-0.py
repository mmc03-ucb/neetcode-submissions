class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        arrSet = set()

        l = 0

        for r in range(len(nums)):
            if nums[r] in arrSet:
                return True

            arrSet.add(nums[r])
            if r - l == k:
                arrSet.remove(nums[l])
                l += 1
            

        return False 