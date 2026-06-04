# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.max_depth = 0
        self.findMaxDepth(root, 0)
        self.cool_root = None
        self.findSubtree(root, 0)
        return self.rootes
    
    def findSubtree(self, root, depth):
        if root is None:
            return False
        if depth == self.max_depth:
            return True
        left_subtree = self.findSubtree(root.left, depth + 1)
        right_subtree = self.findSubtree(root.right, depth + 1)
        if left_subtree or right_subtree:
            return True
            

    def findMaxDepth(self, root, depth) -> int:
        if root.left is None and root.right is None:
            self.max_depth = max(self.max_depth, depth)
            return
        if root.left:
            self.findMaxDepth(root.left, depth + 1)
        if root.right:
            self.findMaxDepth(root.right, depth + 1)