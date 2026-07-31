class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxNums = max(nums)
        if maxNums < 0:
            return maxNums
        
        maxSum = 0
        currSum = 0
        for num in nums:
            currSum = max(currSum + num, 0)
            maxSum = max(maxSum, currSum)
        
        return maxSum