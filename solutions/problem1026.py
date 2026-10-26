# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode | None) -> int:
        self.res = 0
        self.recurse(root)
        return self.res

    def recurse(self, root):
        if root is None:
            return []
        left_res = self.recurse(root.left)
        right_res = self.recurse(root.right)
        left_res.extend(right_res)
        compare = left_res
        for val in compare:
            self.res = max(self.res, abs(root.val - val))
        compare.append(root.val)
        return compare