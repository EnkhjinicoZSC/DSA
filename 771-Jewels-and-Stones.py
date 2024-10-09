class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel = defaultdict(bool)
        for each in jewels:
            jewel[each] = True
        
        count = 0
        for stone in stones:
            if stone in jewel:
                count += 1
        return count