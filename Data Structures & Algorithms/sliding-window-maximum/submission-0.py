class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        naive:
        for each window, call max O(n^2)
        optimizations:
        maintain a heap. O(logn)
        Overall TC: nlogn
        include num and index to check if num is valid -> pop nums with invalid index to get largest remaining valid num
        start appending to output when r >= k - 1
        """

        l = 0
        output = []
        heap = []

        for r in range(len(nums)):
            heapq.heappush_max(heap, (nums[r], r))
            while heap[0][1] <= r - k:
                heapq.heappop_max(heap)
            
            if r >= k - 1:
                output.append(heap[0][0])
        
        return output
        
        """
        r = 4
        heap = [(1,0), (2,1), (1,2), (0,3), (1,4), (5,2)]
        output = [2, 2, 4, 4, 6]
        """