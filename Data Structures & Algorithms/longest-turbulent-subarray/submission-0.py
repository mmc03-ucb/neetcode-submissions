class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """
        sliding window variable size
        loop through each element and compare to previous while keeping track of comparison sign
        if comparison sign flips, continue
        elif same comparison sign window starts at i - 1
        else window starts at i (same element)
        """
        sign = ""

        l = 0
        length = 1

        for r in range(1, len(arr)):
            if arr[r] - arr[r-1] > 0:
                curr = "+"
            elif arr[r] - arr[r-1] < 0:
                curr = "-"
            else:
                curr = "0"
            
            if curr == "0":
                l = r
                sign = ""
            elif sign == curr:
                l = r - 1
                sign = curr
            else:
                length = max(length, r-l + 1)
                sign = curr
        
        return length

        