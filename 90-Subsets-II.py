class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(curr, i):
            if i > len(nums):
                return 
            if curr not in res:
                res.append(curr.copy())
            for j in range(i, len(nums)):
                curr.append(nums[j])
                backtrack(curr, j + 1)
                curr.pop()
                
        backtrack([], 0)
        return res
