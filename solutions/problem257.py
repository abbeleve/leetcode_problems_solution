# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from copy import copy

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.res = []
        self.recurse(root, [])
        return self.res

    def recurse(self, root, path):
        path.append(root.val)
        if root.left:
            self.recurse(root.left, copy(path))
        if root.right:
            self.recurse(root.right, copy(path))
        if root.left is None and root.right is None:
            self.res.append("->".join(str(val) for val in path))