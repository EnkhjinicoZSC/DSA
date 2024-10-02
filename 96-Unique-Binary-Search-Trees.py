class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def dp(n):
            if n < 2:
                return 1
            ans = 0
            for i in range(1, n + 1):
                ans += dp(i-1) * dp(n-i)
            return ans
        
        return dp(n)

        