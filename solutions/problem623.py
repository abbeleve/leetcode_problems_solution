# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        self.nodes = []
        self.val = val
        self.depth = depth
        self.max_depth = 1
        # self.get_max_depth(root, 1)
        # if self.max_depth < self.depth:
            # self.depth = self.max_depth
        if self.depth != 1:
            self.find_depth(root, 1)
        else:
            new_node = TreeNode(val=val, left=root)
            root = new_node
            return root

        for node in self.nodes:
            new_node = TreeNode(val=val, left=node.left)
            node.left = new_node
            new_node = TreeNode(val=val, right=node.right)
            node.right = new_node
        return root

    def get_max_depth(self, root, depth):
        if root is None:
            return
        self.max_depth = max(self.max_depth, depth)
        self.get_max_depth(root.left, depth + 1)
        self.get_max_depth(root.right, depth + 1)

    def find_depth(self, root, depth):
        if root is None:
            return
        if depth == self.depth - 1:
            self.nodes.append(root)
        self.find_depth(root.left, depth + 1)
        self.find_depth(root.right, depth + 1)