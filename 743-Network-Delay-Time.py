class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            adj[u].append([v, w])

        h = [[0, k]]
        visit = set()
        while h:
            weight, node = heapq.heappop(h)
            if node in visit:
                continue
            visit.add(node)
            if len(visit) == n:
                return weight
            for nei, wei in adj[node]:
                if nei not in visit:
                    heapq.heappush(h, [(weight + wei), nei])
        return -1