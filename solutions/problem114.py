class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        stack = self.pre_order_traversal(root, [])
        

    def pre_order_traversal(self, root, stack):
        if root.left is None and root.right is None:
            return root.val
        stack.append(root.val)
        stack = self.pre_order_traversal(root.left)
        stack = self.pre_order_traversal(root.right)
        return stack