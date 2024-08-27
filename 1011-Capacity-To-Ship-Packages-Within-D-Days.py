class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def helper(mid):
            day, currMid = 1, mid
            for w in weights:
                if currMid - w < 0:
                    day += 1
                    currMid = mid
                currMid -= w
            return day <= days

        while l <= r:
            mid = (l + r) // 2
            if helper(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res