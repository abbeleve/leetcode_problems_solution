# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.to_delete = to_delete
        self.to_delete.append(1001)
        self.deleted_nodes = []
        root = TreeNode(val=1001, left=root)
        self.recurse(root)
        return self.deleted_nodes

    def recurse(self, root):
        if root is None:
            return
        left = root.left
        right = root.right
        if root.val in self.to_delete:
            if root.left is not None and left.val not in self.to_delete:
                self.deleted_nodes.append(left)
                root.left = None
            if root.right is not None and right.val not in self.to_delete:
                self.deleted_nodes.append(right)
                root.right = None
        self.recurse(left)
        self.recurse(right)

        if left is not None and left.val in self.to_delete:
            root.left = None
        if right is not None and right.val in self.to_delete:
            root.right = None