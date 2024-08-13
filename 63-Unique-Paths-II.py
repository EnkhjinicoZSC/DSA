class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        @cache
        def dp(i, j):
            if obstacleGrid[i][j]:
                return 0
            if i == 0 and j == 0:
                return 1
            if i == 0:
                return dp(i, j - 1)
            if j == 0:
                return dp(i - 1, j)
            
            return dp(i-1, j) + dp(i, j-1)
        return dp(rows - 1, cols - 1)
