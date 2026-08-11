class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for p in points:
            x = p[0]
            y = p[1]

            dist = (abs(x-0) ** 2) + abs((y-0) ** 2)
            heapq.heappush(heap, (-dist, [x,y]))

            if len(heap) > k:
                heapq.heappop(heap)
        
        output = []
        while heap:
            output.append(heapq.heappop(heap)[1])
        
        return output