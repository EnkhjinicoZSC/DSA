# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        adj = defaultdict(list)
        res = ""
        def dfs(node):
            if not node: return
            if node.left:
                adj[node.val].append((node.left.val, "L"))
                adj[node.left.val].append((node.val, "U"))
                dfs(node.left)
            if node.right:
                adj[node.val].append((node.right.val, "R"))
                adj[node.right.val].append((node.val, "U"))
                dfs(node.right)
        
        dfs(root)
        q = deque([(startValue, "")])
        seen = set([startValue])

        while q:
            node, path = q.popleft()
            if node == destValue:
                return path
            for nei, dir in adj[node]:
                if nei not in seen:
                    seen.add(nei)
                    q.append((nei, path + dir))

        return ""
