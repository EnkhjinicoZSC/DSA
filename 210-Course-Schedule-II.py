class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegrees = [0] * numCourses
        visit = set()
        topo_order = []

        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegrees[crs] += 1

        q = deque()

        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        
        count = 0
        while q:
            node = q.popleft()
            topo_order.append(node)
            count += 1
            for nei in adj[node]:
                indegrees[nei] -= 1

                if indegrees[nei] == 0:
                    q.append(nei)

        return topo_order if count == numCourses else []