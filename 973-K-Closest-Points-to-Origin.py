class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for point in points:
            x, y = point
            heapq.heappush(minheap, [((x ** 2 + y ** 2) ** 0.5), x, y])
        res = []
        while k > 0:
            k -= 1
            point = heapq.heappop(minheap)
            res.append([point[1], point[2]])
        return res