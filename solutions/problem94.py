# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.traversal(root)
        return self.res

    def traversal(self, root):
        if root is None:
            return
        self.traversal(root.left)
        self.res.append(root.val)
        self.traversal(root.right)