class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxFruits = 0
        counts = Counter()

        l = 0

        for r in range(len(fruits)):
            counts[fruits[r]] += 1

            while len(counts) > 2:
                counts[fruits[l]] -= 1
                if counts[fruits[l]] == 0:
                    del counts[fruits[l]]
                l += 1
            
            maxFruits = max(maxFruits, r - l + 1)
        
        return maxFruits