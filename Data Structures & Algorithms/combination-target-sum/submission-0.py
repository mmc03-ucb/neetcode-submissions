class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        combs = []

        def backtrack(i, comb, total):
            if total == target:
                combs.append(comb.copy())
                return
            elif total > target or i >= len(nums):
                return
            
            comb.append(nums[i])
            total += nums[i]
            backtrack(i, comb, total)

            total -= comb.pop()
            backtrack(i+1, comb, total)
        
        backtrack(0, [], 0)

        return combs