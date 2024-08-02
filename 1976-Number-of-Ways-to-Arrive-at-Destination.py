class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        minV = float("-inf")
        for u, v, c in roads:
            adj[u].append((v, c))
            adj[v].append((u, c))


        distances = [float("inf")] * n
        distances[0] = 0
        ways = [0] * n
        ways[0] = 1
        minH = [(0, 0)] # cost, node

        while minH:
            cost, node = heapq.heappop(minH)
            if cost > distances[node]: continue
            
            for nei, neiCost in adj[node]:
                if neiCost + cost < distances[nei]:
                    distances[nei] = neiCost + cost
                    ways[nei] = ways[node]
                    heapq.heappush(minH, (neiCost + cost, nei))
                elif neiCost + cost == distances[nei]:
                    ways[nei] = (ways[nei] + ways[node]) % (10 ** 9 + 7)

        return ways[-1]




