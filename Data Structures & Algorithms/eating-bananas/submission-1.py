import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        binary search between minSpeed and maxSpeed
        maxSpeed = max(piles)
        minSpeed = 1
        for each speed:
            time = 0
            for p in piles:
                time += math.ceil(p / s)
                if time > h:
                    increase speed
            k = min(k, speed)
            decrease speed
        """

        low = 1
        high = max(piles)  # O(n)
        k = float("INF")

        while low <= high:  # O(logn)
            s = low + (high - low) // 2
            print(s)
            time = 0
            for p in piles:  # O(n)
                time += math.ceil((p / s))
            
            if time > h:
                low = s + 1
            else:
                high = s - 1
                k = min(k, s)

        return k
