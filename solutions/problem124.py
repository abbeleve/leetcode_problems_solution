# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = -10**13
        self.pathCounter(root)
        return self.maxPath

    def pathCounter(self, root):
        if root.left is None and root.right is None:
            self.maxPath = max(self.maxPath, root.val)
            return root.val
        max_local_sum = root.val
        if root.left:
            left_counter = self.pathCounter(root.left)
            max_local_sum = max(max_local_sum, root.val + left_counter)
        if root.right:
            right_counter = self.pathCounter(root.right)
            max_local_sum = max(max_local_sum, root.val + right_counter)
        if root.left and root.right:
            max_sum = max(left_counter + root.val, right_counter + root.val, left_counter + right_counter + root.val, root.val)
            self.maxPath = max(self.maxPath, max_sum)
        self.maxPath = max(self.maxPath, max_local_sum)
        return max_local_sum