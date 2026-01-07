# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        stack = []
        if root is None:
            return False
        return self.iterate(root, targetSum, stack)
    
    def iterate(self, root, targetSum, stack):
        if root.left is None and root.right is None:
            stack.append(root.val)
            return True if sum(stack) == targetSum else False
        if root.left or root.right:
            stack.append(root.val)
        if root.left:    
            if self.iterate(root.left, targetSum, stack):
                return True
            stack.pop()
        if root.right:
            if self.iterate(root.right, targetSum, stack):
                return True
            stack.pop()
        return False