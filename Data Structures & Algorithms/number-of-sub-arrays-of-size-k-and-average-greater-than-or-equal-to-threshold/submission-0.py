class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        count = 0
        running = 0
        
        for r in range(len(arr)):
            running += arr[r]
            if r - l + 1 == k:
                if running / k >= threshold:
                    count += 1
                
                running -= arr[l]
                l += 1
        
        return count