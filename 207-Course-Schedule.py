class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        visit = set()

        for crs, pre in prerequisites:
            adj[crs].append(pre)
        def dfs(crs):
            if crs in visit:
                return False
            if adj[crs] == []: return True
            visit.add(crs)
            for child in adj[crs]:
                if not dfs(child):
                    return False
            visit.remove(crs)
            adj[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True





            

