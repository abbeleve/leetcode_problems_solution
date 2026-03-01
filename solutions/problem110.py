# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.task = True
        self.height_search(root, 0)
        return self.task

    def height_search(self, root, depth):
        if root is None:
            return depth - 1
        left_subtree_depth = self.height_search(root.left, depth + 1)
        right_subtree_depth = self.height_search(root.right, depth + 1)
        if abs(right_subtree_depth - left_subtree_depth) > 1:
            self.task = False
            return 10**9
        return max(left_subtree_depth, right_subtree_depth)