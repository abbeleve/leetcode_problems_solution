# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        stack = [[root, root.val]]
        path_list = [[root]]
        result = []
        while len(stack) > 0:
            node, val = stack.pop(0)
            if node.left:
                stack.append([node.left, node.left.val + val])

            if node.right:
                stack.append([node.right, node.right.val + val])
            if node.left is None and node.right is None:
                if 