class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []

        def backtrack(i, subset):
            if i == len(nums):
                subsets.append(subset.copy())
                return
            
            # include
            subset.append(nums[i])
            backtrack(i+1, subset)

            # exclude
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            backtrack(i+1, subset)
        
        backtrack(0, [])

        return subsets