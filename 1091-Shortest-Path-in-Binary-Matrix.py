class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        rows, cols = len(grid), len(grid[0])

        if grid[0][0] != 0 or grid[rows - 1][cols - 1] != 0:
            return -1

        def isValid(r, c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0:
                return True
            return False

        q = deque([((0, 0), 1)])
        visited = set()
        visited.add((0, 0))
        while q:
            (r, c), steps = q.popleft()
            if (r, c) == (rows - 1, cols - 1):
                return steps
            for i, j in dirs:
                next_r, next_c = i + r, j + c
                if isValid(next_r, next_c) and (next_r, next_c) not in visited:
                    visited.add((next_r, next_c))
                    q.append(((next_r, next_c), steps + 1))
        return -1

        

        # [0,1,1,1,1,1,1,1],
        # [0,1,1,0,0,0,0,0],
        # [0,1,0,1,1,1,1,0],
        # [0,1,0,1,1,1,1,0],
        # [0,1,1,0,0,1,1,0],
        # [0,1,1,1,1,0,1,0],
        # [0,0,0,0,0,1,1,0],
        # [1,1,1,1,1,1,1,0]]