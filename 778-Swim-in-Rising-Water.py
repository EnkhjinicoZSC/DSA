class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        minheap = [[grid[0][0], (0, 0)]]
        res = 0
        seen = set((0, 0))

        def check_boundary(i, j):
            return 0 <= i < rows and 0 <= j < cols

        while minheap:
            nodeVal, (r, c) = heapq.heappop(minheap)
            res = max(res, nodeVal)
            if (r, c) == (rows - 1, cols - 1):
                return res
            for dr, dc in dirs:
                next_r, next_c = r + dr, c + dc
                if check_boundary(next_r, next_c) and (next_r, next_c) not in seen:
                    seen.add((next_r, next_c))
                    heapq.heappush(minheap, [grid[next_r][next_c], (next_r, next_c)])

        return -1 


