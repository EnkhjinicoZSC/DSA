class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node, parent):
            time = 0
            for child in adj[node]:
                if child != parent:
                    child_time = dfs(child, node)
                    if child_time > 0 or hasApple[child]:
                        time += child_time + 2
            return time
        
        return dfs(0, -1)