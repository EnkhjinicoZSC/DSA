class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = set()
        rows, cols = len(board), len(board[0])

        def helper(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def dfs(i, j, k):
            if k == len(word):
                return True
            
            if not helper(i, j) or (i, j) in visited or board[i][j] != word[k]:
                return False

            visited.add((i, j))
            for dr, dc in directions:
                if dfs(i+dr, j+dc, k + 1):
                    return True
            visited.remove((i, j))
            return False

        count = {}
        for c in word:
            count[c] = 1 + count.get(c, 0)
            
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): return True
        return False