class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)

        for i in range(len(edges)):
            adj[edges[i][0]].append((edges[i][1], succProb[i]))
            adj[edges[i][1]].append((edges[i][0], succProb[i]))
        seen = set()
        h = [[-1, start_node]]
        while h:
            prob, node = heapq.heappop(h)
            if node == end_node:
                return -prob
            seen.add(node)
            for nei, neiCost in adj[node]:
                if nei not in seen:
                    heapq.heappush(h, [neiCost*prob, nei])
        return 0
