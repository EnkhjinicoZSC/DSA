class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums: return 0
        dp = {0: 1}
        for i in range(1, target + 1):
            dp[i] = 0
            for n in nums:
                dp[i] += dp.get(i-n, 0)
        return dp[target]
                