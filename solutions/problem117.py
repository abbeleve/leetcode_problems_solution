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
    def connect(self, root: 'Node') -> 'Node':
        tree_hash_table = {}
        tree_hash_table = self.iterate(root, tree_hash_table, 0)
        keys = tree_hash_table.keys()
        for depth in keys:
            for index, node in enumerate(tree_hash_table[depth][:-1]):
                node.next = tree_hash_table[depth][index + 1]
        return root

    def iterate(self, root, tree_hash_table, depth):
        if root is None:
            return tree_hash_table
        if depth not in tree_hash_table:
            tree_hash_table[depth] = [root]
        else:
            tree_hash_table[depth].append(root)
        tree_hash_table = self.iterate(root.left, tree_hash_table, depth + 1)
        tree_hash_table = self.iterate(root.right, tree_hash_table, depth + 1)
        return tree_hash_table