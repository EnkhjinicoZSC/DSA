class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # 1, 2, 3, 4, 3, 2, 1 || 1, 2, 3, 4, 2, 7
        m, n = len(nums1), len(nums2)
        dp = [[0] * n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    if i > 0 and j > 0:
                        dp[i][j] = 1 + dp[i - 1][j - 1]
                    else:
                        dp[i][j] = 1
                    res = max(res, dp[i][j])
        return res

                        