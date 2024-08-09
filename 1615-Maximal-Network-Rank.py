class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        road_count = [0] * n
        direct_road = set()
        
        for u, v in roads:
            road_count[u] += 1
            road_count[v] += 1
            direct_road.add((u, v))
            direct_road.add((v, u))
        
        max_rank = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                rank = road_count[i] + road_count[j]
                if (i, j) in direct_road:
                    rank -= 1
                max_rank = max(max_rank, rank)
        
        return max_rank