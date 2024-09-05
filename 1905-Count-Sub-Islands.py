class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        res = 0
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        rows, cols = len(grid1), len(grid1[0])
        visit = set()
        num_islands = 0
        

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid2[r][c] == 0 or (r, c) in visit:
                return True 
            visit.add((r, c))
            check = True
            if not grid1[r][c]:
                check = False
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                check = dfs(nr, nc) and check

            return check
                
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] and (r, c) not in visit:
                    if dfs(r, c):
                        num_islands += 1

        return num_islands