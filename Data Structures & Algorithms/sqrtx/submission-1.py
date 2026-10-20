class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        lower = float("INF")

        while l <= r:
            m = (l + r) // 2
            prod = m * m
            if prod <= x:
                lower = m
                l = m + 1
            else:
                r = m - 1
        return lower