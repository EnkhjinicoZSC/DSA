class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        res = []
        for each in queries:
            idx = bisect.bisect_right(nums, each)
            res.append(idx)
        return res