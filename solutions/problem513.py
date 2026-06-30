# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        return self.iterate(root, 0)[0]

    def iterate(self, root, depth):
        if root.left is None and root.right is None:
            return root.val, depth
        left_elem, left_elem_depth, right_elem, right_elem_depth = None, None, None, None
        if root.left:
            left_elem, left_elem_depth = self.iterate(root.left, depth + 1)
        if root.right:
            right_elem, right_elem_depth = self.iterate(root.right, depth + 1)
        if left_elem is not None and right_elem is not None:
            if left_elem_depth >= right_elem_depth:
                return left_elem, left_elem_depth
            return right_elem, right_elem_depth
        if left_elem is not None:
            return left_elem, left_elem_depth
        if right_elem is not None:
            return right_elem, right_elem_depth