# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = []
        return self.iterate(root, stack, 0)

    def iterate(self, root, stack, result_sum):
        stack.append(root.val)
        if root.left is None and root.right is None:
            num = 0
            for index, i in enumerate(stack[::-1]):
                num += i * (10**index)
            result_sum += num
            return result_sum
        if root.left:
            result_sum = self.iterate(root.left, stack, result_sum)
            stack.pop()
        if root.right:
            result_sum = self.iterate(root.right, stack, result_sum)
            stack.pop()
        return result_sum