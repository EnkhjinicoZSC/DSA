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



        # [1, 2, 3]
        # output: [], [1], [1, 2], [1, 3], [2], [2, 3], [1, 2, 3]
        #  [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        # [1, 2, 2]
        # [], [1], [1, 2], [1, 2, 2], [2], [2, 2]
