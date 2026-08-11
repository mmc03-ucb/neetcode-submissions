class Solution:
    def trap(self, height: List[int]) -> int:
        """
        water[i] = min(leftMax, rightMax) - height[i] where 
        leftMax, rightMax is inclusive of height[i]
        one pass for leftMax
        one pass for rightMax
        sum over i for area
        """

        lMax = 0
        leftMax = []
        for l in height:
            lMax = max(l, lMax)
            leftMax.append(lMax)
        
        area = 0
        rMax = 0
        for r in range(len(height) -1, -1, -1):
            rMax = max(rMax, height[r])
            water = min(leftMax[r], rMax) - height[r]
            area += water
        
        return area