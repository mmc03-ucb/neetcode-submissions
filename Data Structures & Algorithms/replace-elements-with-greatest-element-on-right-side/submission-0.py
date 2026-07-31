class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        reverse iterate from right keeping track of max
        """
        maxR = 0
        for r in range(len(arr) -1, -1, -1):
            # last elem
            if r == len(arr) - 1:
                maxR = arr[r]
                arr[r] = -1
            else:
                temp = arr[r]
                arr[r] = maxR
                maxR = max(temp, maxR)
        
        return arr