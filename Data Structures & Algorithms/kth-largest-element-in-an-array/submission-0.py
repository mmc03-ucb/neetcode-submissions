class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0][0]