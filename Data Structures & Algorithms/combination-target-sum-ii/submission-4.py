class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        combs = []

        def bt(i, comb, total):
            if total == target:
                combs.append(comb.copy())
                return
            elif total > target or i >= len(candidates):
                return
            
            comb.append(candidates[i])
            bt(i+1, comb, total + candidates[i])

            comb.pop()

            while i+1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            
            bt(i+1, comb, total)

            return
        
        bt(0, [], 0)

        return combs