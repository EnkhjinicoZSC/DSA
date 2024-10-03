class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        @cache
        def dp(i, holding):
            if i == len(prices):
                return 0
            ans = dp(i+1, holding)
            if holding:
                # we can sell or skip
                sell = prices[i] - fee + dp(i+1, False)
                ans = max(ans, sell)
            else:
                # skip or buy
                buy = -prices[i] + dp(i+1, True)
                ans = max(ans, buy)
            return ans

        return dp(0, False)