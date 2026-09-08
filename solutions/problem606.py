# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.traverse(root)
    
    def traverse(self, root):
        magical_string = ""
        magical_string += str(root.val)
        if root.left is not None:
            left_magical_string = self.traverse(root.left)
            magical_string += "(" + left_magical_string + ")"
        if root.right is not None:
            right_magical_string = self.traverse(root.right)
            if root.left is None:
                magical_string += "()"
            magical_string += "(" + right_magical_string + ")"
        return magical_string