# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        self.min_depth = 10**9
        self.recurse(root, 1)
        return self.min_depth

    def recurse(self, root, depth):
        if root.left is None and root.right is None:
            self.min_depth = min(self.min_depth, depth)
            return
        if root.left is not None:
            self.recurse(root.left, depth + 1)
        if root.right is not None:
            self.recurse(root.right, depth + 1)