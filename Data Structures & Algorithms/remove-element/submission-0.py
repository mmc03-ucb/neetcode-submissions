class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        two pointers
        if the current num is not val:
            swap values between pointers
            increment both pointers
        else:
            increment only 1 pointer
        """

        l, r = 0, 0

        for r in range(len(nums)):
            if nums[r] != val:
                nums[r], nums[l] = nums[l], nums[r]
                r += 1
                l += 1
            else:
                r += 1
        
        return l