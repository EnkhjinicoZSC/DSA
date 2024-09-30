class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            elif rank[p1] < rank[p2]:
                parent[p1] = p2
            elif rank[p1] > rank[p2]:
                parent[p2] = p1
            else:
                parent[p2] = parent[p1]
                rank[p1] += 1
            return True

        for edge in edges:
            if not union(edge[0], edge[1]):
                return edge 