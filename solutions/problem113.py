# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        self.targetSum = targetSum
        self.result = []
        self.dfs(root, 0, [])
        return self.result
    
    def dfs(self, node, sum, path):
        sum += node.val
        path.append(node.val)
        if node.left:
            self.dfs(node.left, sum, path)
        if node.right:
            self.dfs(node.right, sum, path)
        if node.left is None and node.right is None:
            if sum == self.targetSum:
                self.result.append(path[:])
        sum -= node.val
        path.pop()