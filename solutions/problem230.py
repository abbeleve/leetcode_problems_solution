# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = self.pathingThroughTree(root, [])
        return stack[k - 1]

    def pathingThroughTree(self, root, stack):
        if root.left:
            stack = self.pathingThroughTree(root.left, stack)
        stack.append(root.val)
        if root.right:
            stack = self.pathingThroughTree(root.right, stack)
        return stack