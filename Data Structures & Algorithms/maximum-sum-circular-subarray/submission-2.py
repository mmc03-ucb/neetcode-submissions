class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax, globMin = nums[0], nums[0]
        currMax, currMin = 0, 0
        total = 0

        for num in nums:
            total += num
            currMax = max(num, currMax + num)
            currMin = min(num, currMin + num)

            globMax = max(currMax, globMax)
            globMin = min(currMin, globMin)

        
        return max(globMax, total - globMin) if globMax > 0 else globMax