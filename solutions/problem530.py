# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = self.pathingThroughTree(root, [])
        minimal = 10**9
        for index in range(len(stack) - 1):
            ranging = stack[index + 1] - stack[index]
            minimal = min(minimal, ranging)
        return minimal 

    def pathingThroughTree(self, root, stack):
        if root.left:
            stack = self.pathingThroughTree(root.left, stack)
        stack.append(root.val)
        if root.right:
            stack = self.pathingThroughTree(root.right, stack)
        return stack