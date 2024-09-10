class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append([v, w])
            adj[v].append([u, w])
        
        distToLastNode = self.dijkstra(n, adj)

        @cache
        def dfs(node):
            if node == n:
                return 1
            res = 0
            for nei, wei in adj[node]:
                if distToLastNode[node] > distToLastNode[nei]:
                    res = (res+ dfs(nei)) % (10**9 + 7)

            return res

        return dfs(1)



    def dijkstra(self, n, adj):
        pq = [(0, n)]
        dist = [float('inf')] * (n + 1)
        dist[n] = 0 
        
        while pq:
            d, node = heapq.heappop(pq)
            
            if d > dist[node]:
                continue
            
            for neighbor, weight in adj[node]:
                new_dist = d + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
        
        return dist