class Solution:
    def trap(self, height: List[int]) -> int:
        # water[i] = min(maxL, maxR) - height[i]

        l, r = 0, len(height) - 1
        maxl, maxr = 0, 0
        water = 0

        while l <= r:
            maxl = max(height[l], maxl)
            maxr = max(height[r], maxr)

            if maxl <= maxr:
                water += maxl - height[l]
                l += 1
            else:
                water += maxr - height[r]
                r -= 1
        
        return water
