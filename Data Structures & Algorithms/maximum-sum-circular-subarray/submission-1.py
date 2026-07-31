class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        maxSubarray = max(regular, circular)
        regular = globMax
        circular = total - globMin
        if globMax <= 0:
            return globMax
        """

        currMax, currMin, globMax, globMin = 0,0,nums[0],nums[0]
        total = 0

        for num in nums:
            total += num
            currMax = max(currMax + num, num)
            currMin = min(currMin + num, num)

            globMax = max(globMax, currMax)
            globMin = min(globMin, currMin)
        
        return max(globMax, total - globMin) if globMax > 0 else globMax