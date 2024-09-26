class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr, i):
            if i > len(nums):
                return 
            
            res.append(curr.copy())
            for j in range(i, len(nums)):
                curr.append(nums[j])
                backtrack(curr, j + 1)
                curr.pop()
                
        backtrack([], 0)
        return res