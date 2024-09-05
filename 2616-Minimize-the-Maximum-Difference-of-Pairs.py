class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        l, r = 0, max(nums)
        nums.sort()
        if p == 0: return 0
        def is_valid(th):
            i, cnt = 0, 0
            while i < len(nums) - 1:
                if abs(nums[i]-nums[i+1]) <= th:
                    cnt += 1
                    i += 2
                else:
                    i += 1
                if cnt == p: return True
            return False 

        res = 10**9
        while l <= r:
            mid = l + (r - l) // 2
            if is_valid(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
