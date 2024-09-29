class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def backtrack(row, diagonals, anti_diagonals, cols, board):
            if row == n:
                res.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col
                if (col in cols
                    or curr_diagonal in diagonals
                    or curr_anti_diagonal in anti_diagonals):
                    continue
                
                cols.add(col)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)
                board[row][col] = "Q"

                backtrack(row + 1, diagonals, anti_diagonals, cols, board)

                cols.remove(col)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)
                board[row][col] = "."

        board = [["." for _ in range(n)] for _ in range(n)]
        backtrack(0, set(), set(), set(), board)
        return res