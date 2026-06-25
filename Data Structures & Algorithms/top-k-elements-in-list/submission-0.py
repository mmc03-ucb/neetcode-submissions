class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Initialize a dictionary where key is num and count is count of num in nums
        Loop through nums and update dictionary counts
        initialize minHeap
        loop through dictionary and add (count, num) to heap
        if len(heap) == k and currCount > count:
            heapq.heappushpop(minHeap, (currCount, num))
        
        output = []
        loop through heap and add num to output
        return output
        TC: O(nlogk)
        SC: max(k, unique(nums))
        """

        numCount = defaultdict(int)
        for num in nums:
            numCount[num] += 1
        
        minHeap = []

        for num, count in numCount.items():
            if len(minHeap) == k:
                heapq.heappushpop(minHeap, (count, num))
            else:
                heapq.heappush(minHeap, (count, num))
        
        output = []
        while len(minHeap) > 0:
            count, num = heapq.heappop(minHeap)
            output.append(num)
        
        return output