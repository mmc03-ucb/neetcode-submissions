class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0, 0, 0]
        for num in nums:
            buckets[num] += 1
        
        ix = 0
        for i in range(3):
            count = buckets[i]
            for _ in range(count):
                nums[ix] = i
                ix += 1
        
        