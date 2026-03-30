# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.path(root)

    def path(self, root):
        left_sum, right_sum = None, None
        if root.left:
            left_sum = self.path(root.left)
        if root.right:
            right_sum = self.path(root.right)
        if left_sum and right_sum:
            
        if root.left is None and root.right is None:
            return root.val