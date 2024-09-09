class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        adj = defaultdict(list)
        n = len(quiet)

        for u, v in richer:
            adj[v].append(u)
        res = [-1] * n
        def dfs(i):
            if res[i] != -1:
                return res[i]
            res[i] = i
            for rich in adj[i]:
                cand = dfs(rich)
                if quiet[cand] < quiet[res[i]]:
                    res[i] = cand
            return res[i]

        for i in range(n):
            dfs(i)
        return res