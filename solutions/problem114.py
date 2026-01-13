class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        stack = self.pre_order_traversal(root, [])
        save_root = root
        for node in stack[1:]:
            root.left = None
            root.right = node
            root = root.right
        return save_root
        
    def pre_order_traversal(self, root, stack):
        if root is None:
            return stack
        stack.append(root)
        stack = self.pre_order_traversal(root.left, stack)
        stack = self.pre_order_traversal(root.right, stack)
        return stack