class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        q = collections.deque()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = \#\

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    next_r, next_c = r + dr, c + dc
                    if 0 <= next_r < rows and 0 <= next_c < cols and mat[next_r][next_c] == \#\:
                        mat[next_r][next_c] = mat[r][c] + 1
                        q.append((next_r, next_c))
        
        return mat

