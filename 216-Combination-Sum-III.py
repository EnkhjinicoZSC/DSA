class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(curr, i, total):
            if len(curr) == k and total == n:
                res.append(curr.copy())
                return
            
            if len(curr) > k or total > n:
                return

            for num in range(i, 10):
                curr.append(num)
                backtrack(curr, num + 1, total + num)
                curr.pop()
        
        backtrack([], 1, 0)
        return res
