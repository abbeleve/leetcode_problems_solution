class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        save = root.left
        root.left = root.right
        root.right = save

        return root