# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = self.bfs(root)
        return result[::-1]
        
    def bfs(self, root):
        stack = [root]
        result = []
        level = 0
        hash_map = {root: 0}
        while len(stack) > 0:
            node = stack.pop(0)
            node_level = hash_map[node]
            if len(result) - 1 < node_level:
                result.append([])
            result[node_level].insert(0, node.val)
            if node.right:
                stack.append(node.right)
                hash_map[node.right] = hash_map[node] + 1
                level = max(level, hash_map[node] + 1)
            if node.left:
                stack.append(node.left)
                hash_map[node.left] = hash_map[node] + 1
                level = max(level, hash_map[node] + 1)
        return result