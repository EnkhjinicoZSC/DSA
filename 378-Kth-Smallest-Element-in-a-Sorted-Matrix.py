class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for row in matrix:
            for each in row:
                heapq.heappush(heap, each)

        for _ in range(k - 1):
            heapq.heappop(heap)
        
        return heapq.heappop(heap)
