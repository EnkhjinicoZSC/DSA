class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            courseMap[crs].append(pre)

        seen = set()

        def dfs(crs):
            if crs in seen: return False
            if courseMap[crs] == []: return True

            seen.add(crs)

            for nei in courseMap[crs]:
                if not dfs(nei): return False
            seen.remove(crs)
            courseMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True