class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub, i, j):
            while i < j:
                if sub[i] != sub[j]:
                    return False
                i, j = i + 1, j - 1
            return True

        res = []
        path = []

        def dfs(i):
            if i >= len(s):
                res.append(path.copy())
                return 
            for j in range(i, len(s)):
                if is_palindrome(s, i, j):
                    path.append(s[i:j+1])
                    dfs(j+1)
                    path.pop()
            
        dfs(0)
        return res