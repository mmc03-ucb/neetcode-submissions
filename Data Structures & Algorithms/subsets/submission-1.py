class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def dfs(i, subset):
            if i >= len(nums):
                subsets.append(subset.copy())
                return
            
            # exclude
            dfs(i+1, subset)
            # include
            subset.append(nums[i])
            dfs(i+1, subset)
            # remove
            subset.pop()
            return
        
        dfs(0, [])

        return subsets