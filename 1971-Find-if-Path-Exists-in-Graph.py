class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 != p2:
                if rank[p1] > rank[p2]:
                    parent[p2] = p1
                elif rank[p1] < rank[p2]:
                    parent[p1] = p2
                else:
                    parent[p1] = p2
                    rank[p2] += 1

        for u, v in edges:
            union(u, v)
            
        return find(source) == find(destination)