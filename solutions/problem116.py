"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.depth_nodes = {}
        self.traversal(root, 0)
        depth_keys = list(self.depth_nodes.keys())
        for depth in depth_keys:
            for index, node in enumerate(self.depth_nodes[depth][:-1]):
                node.next = self.depth_nodes[depth][index + 1]
        return root
        
    def traversal(self, root, depth):
        if root is None:
            return
        if depth not in self.depth_nodes:
            self.depth_nodes[depth] = [root]
        else:
            self.depth_nodes[depth].append(root)
        self.traversal(root.left, depth + 1)
        self.traversal(root.right, depth + 1)