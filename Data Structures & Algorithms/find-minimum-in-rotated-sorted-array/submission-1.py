class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        inflection point:
        element to left is greater or element to right is smaller
        if first, then element is minimum, if latter, then element to right is minimum
        if not inflection, check whichever half has smaller endpoint
        Edge case: already sorted or just 1 element or all elements same
        """
        if len(nums) == 1 or nums[0] <= nums[-1]:
            return nums[0]

        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r-l) // 2
            print("l, r, m")
            print(l, r, m)
            #inflection point:
            # element to left is greater or element to right is smaller
            if m > 0 and nums[m-1] > nums[m]:
                return nums[m]
            elif m < len(nums) - 1 and nums[m+1] < nums[m]:
                return nums[m+1]
            else:
                if nums[0] <= nums[m] <= nums[-1]:
                    r = m - 1
                elif nums[0] <= nums[m]:
                    l = m + 1
                else:
                    r = m - 1
        
        return nums[m]