class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10 ** 9 + 7
        h = {}
        count = 0
        max_val = 2 ** 21

        for each in deliciousness:
            power = 1
            while power <= max_val:
                complement = power - each
                if complement in h:
                    count += h[complement]
                power = power * 2
            if each in h:
                h[each] += 1
            else:
                h[each] = 1

        return count % MOD
        
