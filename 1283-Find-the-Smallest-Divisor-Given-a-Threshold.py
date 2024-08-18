class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def find_total(div):
            total = 0
            for num in nums:
                total += ceil(num / div)
            return total

        ans, low, high = -1, 1, max(nums)
        
        while low <= high:
            mid = (low + high) // 2
            result = find_total(mid)
            if result <= threshold:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans