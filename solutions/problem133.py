"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        save_node = node
        stack = [Node(node.val)]
        passed_nodes = {}
        while len(stack) > 0:
            elem = stack.pop(0)
            for neighbor in elem.neighbors:
                if stack not in passed_nodes:
                    created_node = Node(neighbor.val)
                    stack.append(created_node)
                    passed_nodes[created_node.val] = created_node
                else:
                    stack.append(passed_nodes[neighbor.val])
        return save_node