class Solution:
    def trap(self, height: List[int]) -> int:
        """
        water[i] = min(leftMax, rightMax) - height[i] where 
        leftMax, rightMax is inclusive of height[i]
        one pass for leftMax
        one pass for rightMax
        sum over i for area
        O(n) TC and SC
        Optimization: SC can be reduced to O(1) using 2 pointers
        l = 0, r = 8
        leftMax = 0, rightMax = 1
        at any i, we only need the min of leftMax and rightMax
        at l, we have trueLeftMax
        at r, we have trueRightMax
        if trueLeft < trueRightMax, increment l
        else: decrement r
        loop termination: l <= r
        """

        l = 0
        r = len(height) - 1
        area = 0
        lMax = 0
        rMax = 0
        while l <= r:
            lMax = max(height[l], lMax)
            rMax = max(height[r], rMax)
            if lMax <= rMax:
                area += lMax - height[l]
                l += 1
            else:
                area += rMax - height[r]
                r -= 1
        
        return area