class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = [[0, 0, 0]]

        def isValid(r, c):
            if 0 <= r < rows and 0 <= c < cols:
                return True
            return False
        visited = set()
        while q:
            diff, r, c = heapq.heappop(q)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if (r, c) == (rows - 1, cols - 1):
                return diff
            for i, j in dirs:
                next_r, next_c = i + r, j + c
                if isValid(next_r, next_c) and (next_r, next_c) not in visited:
                    curr = max(abs(heights[next_r][next_c] - heights[r][c]), diff)
                    heapq.heappush(q, [curr, next_r, next_c])
