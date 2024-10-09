# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = float(\inf\)
        self.arr = []

        def dfs(node):
            if not node: return
            dfs(node.left)
            self.arr.append(node.val)
            dfs(node.right)
        dfs(root)

        print(self.arr)
        for i in range(1, len(self.arr)):
            res = min(res, self.arr[i] - self.arr[i-1])
        return res
        