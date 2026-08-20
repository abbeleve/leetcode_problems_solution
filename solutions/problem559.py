"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.max_depth = 0
        self.recurse(root, 1)
        return self.max_depth

    def recurse(self, root, depth):
        if root is None:
            return
        self.max_depth = max(self.max_depth, depth)
        for children in root.children:
            self.recurse(children, depth + 1)