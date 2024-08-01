class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)
        for u, v, w in flights:
            adj_list[u].append((v, w))
        
        pq = [(0, src, 0)]
        
        costs = {(src, 0): 0}
        
        while pq:
            cost, city, stops = heapq.heappop(pq)
            
            if city == dst:
                return cost
            
            if stops > k:
                continue
            
            for neighbor, price in adj_list[city]:
                new_cost = cost + price
                
                if (neighbor, stops + 1) not in costs or new_cost < costs[(neighbor, stops + 1)]:
                    costs[(neighbor, stops + 1)] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor, stops + 1))
        
        return -1
