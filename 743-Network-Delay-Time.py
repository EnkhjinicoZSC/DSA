class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minH = [[0, k]]
        visited = set()
        adj = {i: [] for i in range(1, n + 1)}
        
        # construct adj
        for u, v, w in times:
            adj[u].append([v, w])

        # Use a variable to track the maximum cost directly
        max_cost = 0
        
        while minH:
            cost, node = heapq.heappop(minH)
            if node in visited:
                continue
            visited.add(node)
            max_cost = max(max_cost, cost)
            for nei, wei in adj[node]:
                if nei not in visited:
                    heapq.heappush(minH, [wei + cost, nei])
        
        # If all nodes are visited, return the max cost, else return -1
        return max_cost if len(visited) == n else -1