# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.targetSum = targetSum
        self.amount = 0
        self.recurse(root)
        return self.amount

    def recurse(self, root):
        if root is None:
            return []
        left_subtree_sum = self.recurse(root.left)
        right_subtree_sum = self.recurse(root.right)
        res = []
        for i in range(len(left_subtree_sum)):
            val = left_subtree_sum[i] + root.val
            if val == self.targetSum:
                self.amount += 1
            res.append(val)

        if root.val == self.targetSum:
            self.amount += 1
        res.append(root.val)
        for i in range(len(right_subtree_sum)):
            val = right_subtree_sum[i] + root.val
            if val == self.targetSum:
                self.amount += 1
            res.append(val)
        
        if root.val == self.targetSum:
            self.amount += 1
        res.append(root.val)
        return res