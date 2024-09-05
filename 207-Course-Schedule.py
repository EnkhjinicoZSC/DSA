class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegrees = [0] * numCourses
        visit = set()

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
            count += 1
            for nei in adj[node]:
                indegrees[nei] -= 1

                if indegrees[nei] == 0:
                    q.append(nei)

        return numCourses == count





            

