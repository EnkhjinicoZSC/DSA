class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dp(i, j):
            if i == 0:
                return 1
            if j == 0:
                return 1

            return dp(i-1, j) + dp(i, j-1)
        return dp(m-1, n-1)
        
