class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))

        seen = set()
        minH = [[-1, start_node]]

        while minH:
            prod, node = heapq.heappop(minH)
            if node == end_node:
                return -prod
            seen.add(node)
            for nei, neiCost in graph[node]:
                if nei not in seen:
                    heapq.heappush(minH, [prod * neiCost, nei])

        return 0

        
