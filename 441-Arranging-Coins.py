class Solution:
    def arrangeCoins(self, n: int) -> int:
        # i = 0
        # while i*(i+1)//2 <= n:
        #     i += 1
        # return i - 1

        l, r = 1, n
        while l <= r:
            mid = (r + l) // 2
            if mid * (mid + 1) // 2 > n:
                r = mid - 1
            elif mid * (mid + 1) // 2 < n:
                l = mid + 1
            else:
                return mid
        return r