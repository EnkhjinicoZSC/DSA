class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        while l <= r:
            mid = (l + r) // 2
            if mid == x // mid:
                return mid
            elif mid > x // mid:
                r = mid - 1
            else:
                l = mid + 1
        return r