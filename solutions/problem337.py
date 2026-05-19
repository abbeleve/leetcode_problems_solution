# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        res = self.recurse(root)
        return max(res[0], res[1])

    def recurse(self, root: Optional[TreeNode]):
        if root is None:
            return 0, 0
        left_res, left_root_res = self.recurse(root.left)
        right_res, right_root_res = self.recurse(root.right)

        return max(left_res + right_res, left_root_res + right_root_res, left_res + right_root_res, right_res + left_root_res), root.val + left_res + right_res