class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        def backtrack(i, num):
            if i == n:
                res.append(num)
                return
            last = num % 10
            next_digits = set([last + k, last - k])

            for next in next_digits:
                if 0 <= next < 10:
                    new_num = num * 10 + next
                    backtrack(i+1, new_num)
        
        res = []
        for num in range(1, 10):
            backtrack(1, num)
        return res
            

