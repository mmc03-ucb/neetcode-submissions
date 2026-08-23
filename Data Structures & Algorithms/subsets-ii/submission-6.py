class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        subsets = []

        def bt(i, subset):
            if i >= len(nums):
                subsets.append(subset.copy())
                return
            
            subset.append(nums[i])
            bt(i+1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            
            bt(i+1, subset)

            return
        
        bt(0, [])

        return subsets