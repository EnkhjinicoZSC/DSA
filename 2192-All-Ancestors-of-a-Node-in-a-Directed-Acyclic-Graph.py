class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        indegree = [0 for _ in range(n)]
        for fro, to in edges:
            adj[fro].append(to)
            indegree[to] += 1
        q = deque([])
        for i in range(n):
            if not indegree[i]:
                q.append(i)
        top_order = []

        while q:
            curr = q.popleft()
            top_order.append(curr)
            for nei in adj[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        res = [[] for _ in range(n)]
        res_set = [set() for _ in range(n)]

        for node in top_order:
            for nei in adj[node]:
                res_set[nei].add(node)
                res_set[nei].update(res_set[node])
        
        for i in range(n):
            for node in range(n):
                if node == i:
                    continue
                if node in res_set[i]:
                    res[i].append(node)

        return res

                    