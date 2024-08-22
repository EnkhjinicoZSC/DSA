class Solution:
    def isHappy(self, n: int) -> bool:
        # 15, 26, 40, 16, 37, 58, 89, 145, 42, 20, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4
        seen = set()
        while n != 1:
            if n in seen: return False
            seen.add(n)
            n = sum((int(i) * int(i)) for i in str(n))
        return True
        
        
        
