# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.travel = []
        self.traversal(root)
        return self.travel

    def traversal(self, root):
        if root is None:
            return
        self.travel.append(root.val)
        self.traversal(root.left)
        self.traversal(root.right)