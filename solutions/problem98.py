# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = self.pathingThroughTree(root, [])
        for index in range(len(stack) - 1):
            if stack[index] >= stack[index + 1]:
                return False
        return True

    def pathingThroughTree(self, root, stack):
        if root.left:
            stack = self.pathingThroughTree(root.left, stack)
        stack.append(root.val)
        if root.right:
            stack = self.pathingThroughTree(root.right, stack)
        return stack