# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        self.levels = {}
        self.recurse(root, 1)
        keys = list(self.levels.keys())
        res = 0
        max_sum = float('-inf')
        for depth in keys:
            if self.levels[depth] > max_sum:
                res = depth
                max_sum = self.levels[depth]
        return res

    def recurse(self, root, depth):
        if root is None:
            return
        self.levels[depth] = self.levels.get(depth, 0) + root.val
        self.recurse(root.left, depth + 1)
        self.recurse(root.right, depth + 1)