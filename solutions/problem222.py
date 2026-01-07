# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        amount_of_nodes = self.iterate(root, 0)
        return amount_of_nodes

    def iterate(self, root, amount_of_nodes):
        if root is None:
            return amount_of_nodes
        amount_of_nodes += 1
        print(root.val)
        amount_of_nodes = self.iterate(root.left, amount_of_nodes)
        amount_of_nodes = self.iterate(root.right, amount_of_nodes)
        return amount_of_nodes