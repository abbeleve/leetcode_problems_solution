class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None:
            return False
        if q is None:
            return False
        stack = self.checkTree(p, [])
        stack2 = self.checkTree(q, [])
        print(stack, stack2)
        if stack == stack2:
            return True
        return False
        
    def checkTree(self, root, stack):
        if root.left is None and root.right is None:
            stack.append(root.val)
            return stack
        if root.left:
            stack = self.checkTree(root.left, stack)
        if root.right:
            stack.append(root.val)
            stack = self.checkTree(root.right, stack)
        print(stack)
        return stack