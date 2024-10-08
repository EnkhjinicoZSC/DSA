class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length = [1] * n
        count = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]
        
        mx = max(length)
        res = 0

        for i in range(n):
            if length[i] == mx:
                res += count[i]
        return res
