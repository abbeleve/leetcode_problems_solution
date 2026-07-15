# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.set_of_subtrees = set()
        self.res = []

    def iterate(self, root, path):
        if root.left is None and root.right is None:
            return root
        if root.left:
            left_node = self.iterate(root.left)
            path.append()
        self.iterate(root.right)