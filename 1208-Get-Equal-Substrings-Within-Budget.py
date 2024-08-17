class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        res = 0
        l = 0
        curr_cost = 0
        for r in range(n):
            curr_cost += abs(ord(t[r]) - ord(s[r]))
            while curr_cost > maxCost:
                curr_cost -= abs(ord(t[l]) - ord(s[l]))
                l += 1
            res = max(res, r - l + 1)
        return res