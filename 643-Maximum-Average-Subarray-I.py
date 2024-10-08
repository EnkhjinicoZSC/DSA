class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        res = curr_sum / k
        for i in range(k, len(nums)):
            curr_sum += nums[i]
            curr_sum -= nums[i-k]

            temp = curr_sum / k
            res = max(res, temp)
        return res