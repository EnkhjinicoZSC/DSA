class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        ans = 0
        dp = [False] * len(s)
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if stack:
                    idx = stack.pop()
                    dp[idx] = True # opening
                    dp[i] = True # closing
        


        print(dp)
        l = 0
        for r in range(len(dp)):
            if dp[r]:
                ans = max(ans, r - l + 1)
            else:
                l = r + 1
        return ans

