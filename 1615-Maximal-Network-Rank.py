class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        res = 0
        for u, v in roads:
            adj[u].append(v)
            adj[v].append(u)
        def helper(i, j):
            redunt = 0
            total = len(adj[i]) + len(adj[j])
            if j in adj[i]:
                redunt += 1
            return total - redunt

        for i in range(n - 1):
            for j in range(i + 1, n):
                res = max(res, helper(i, j))
        
        return res