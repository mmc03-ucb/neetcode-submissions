class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMin, currMax = 0, 0
        globMax, globMin = nums[0], nums[0]

        total = 0

        for num in nums:
            total += num

            currMax = max(num, currMax + num)
            globMax = max(currMax, globMax)

            currMin = min(num, currMin + num)
            globMin = min(currMin, globMin)

        
        return max(total - globMin, globMax) if globMax > 0 else globMax