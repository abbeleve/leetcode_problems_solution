class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSymmetricTwoNodes(root.left, root.right)

    def isSymmetricTwoNodes(self, p, q) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSymmetricTwoNodes(p.left, q.right) and self.isSymmetricTwoNodes(p.right, q.left)