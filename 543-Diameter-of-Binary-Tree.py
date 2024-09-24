# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def depth(root, count):
            if not root:
                return count
            right = depth(root.right, 0)
            left = depth(root.left, 0)
            self.res = max(self.res, right + left)
            return 1 + max(right, left)
        depth(root, 0)
        return self.res