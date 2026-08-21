class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []

        def backtrack(perm, count):
            if len(perm) == len(nums):
                perms.append(perm.copy())
                return
            
            for num in nums:
                if count[num] > 0:
                    perm.append(num)
                    count[num] -= 1
                    backtrack(perm, count)
                    count[num] += 1
                    perm.pop()
        
        backtrack([], Counter(nums))

        return perms
