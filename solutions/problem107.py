# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        hash_map, bfs_traversal, level = self.bfs(root)
        result = [[] for _ in range(level + 1)]
        for i, node in enumerate(bfs_traversal):
            node_level = hash_map[node]
            result[level - node_level].append(node.val)
        for i in result:
            i.sort()
        return result
        
    def bfs(self, root):
        stack = [root]
        result = []
        level = 0
        hash_map = {root: 0}
        while len(stack) > 0:
            node = stack.pop(0)
            node_level = hash_map[node]
            if len(result) < node_level:

            result.append(node)
            if node.right:
                stack.append(node.right)
                hash_map[node.right] = hash_map[node] + 1
                level = max(level, hash_map[node] + 1)
            if node.left:
                stack.append(node.left)
                hash_map[node.left] = hash_map[node] + 1
                level = max(level, hash_map[node] + 1)
        return hash_map, result, level

s = Solution()
print(s.levelOrderBottom())