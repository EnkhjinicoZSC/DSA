class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for weight in stones:
            heappush(heap, -weight)
        while len(heap) > 1:
            stone1, stone2 = heapq.heappop(heap), heapq.heappop(heap)
            if stone1 != stone2:
                heapq.heappush(heap, -(abs(stone1)-abs(stone2)))
        if not heap:
            return 0
        return -heap[0]
