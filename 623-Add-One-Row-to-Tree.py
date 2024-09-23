# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        q = deque([root])
        count = 1

        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node

        while q and count < depth - 1:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            count += 1

        while q:
            node = q.popleft()
            l, r = TreeNode(val), TreeNode(val)
            l.left = node.left
            r.right = node.right

            node.left = l
            node.right = r

        return root