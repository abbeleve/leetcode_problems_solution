class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None:
            return False
        if q is None:
            return False
        stack = self.checkTree(p)
        stack2 = self.checkTree(q)
        print(stack, stack2)
        if stack == stack2:
            return True
        return False
        
    def checkTree(self, root):
        if not root:
            return [None]
        return [root.val] + self.checkTree(root.left) + self.checkTree(root.right)