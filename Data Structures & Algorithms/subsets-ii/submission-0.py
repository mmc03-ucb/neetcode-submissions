class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        currSet, subSets = [], []
        self.helper(0, nums, currSet, subSets)
        return subSets
    
    def helper(self, i, nums, currSet, subSets):
        if i >= len(nums):
            subSets.append(currSet.copy())
            return
        
        currSet.append(nums[i])
        self.helper(i+1, nums, currSet, subSets)

        currSet.pop()
        while i + 1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        self.helper(i+1, nums, currSet, subSets)