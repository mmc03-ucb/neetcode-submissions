class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Create an output array and initialize it with 0s
        initialize a variable prev to 1 (this is the number to the left/right of first and last number)
        loop through nums in order
            output[i] = prev
            prev = nums[i] * prev
        loop through nums in reverse and repeat

        TC: O(n)
        SC: O(1) / O(n) if output array is counted
        """
        left = [0] * len(nums)
        prev = 1

        for i in range(len(nums)):
            left[i] = prev
            prev = nums[i] * prev
        
        prev = 1
        right = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            right[i] = prev
            prev = nums[i] * prev
        
        output = []

        for i in range(len(nums)):
            output.append(left[i] * right[i])
        
        return output
