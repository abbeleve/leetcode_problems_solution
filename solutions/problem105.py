# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        node = None
        for index in range(len(preorder)):
            node_val = preorder[index]
            node = TreeNode(node_val)
            
            inorder.index(node_val)