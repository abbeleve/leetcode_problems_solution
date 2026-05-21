# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.depth_res = {}
        self.traverse(root, 0)
        keys = self.depth_res.keys()
        res = []
        for depth in keys:
            res.append(max(self.depth_res[depth]))
        return res

    def traverse(self, root, depth):
        if root is None:
            return
        if depth not in self.depth_res:
            self.depth_res[depth] = [root.val]
        else:
            self.depth_res[depth].append(root.val)
        self.traverse(root.left, depth + 1)
        self.traverse(root.right, depth + 1)