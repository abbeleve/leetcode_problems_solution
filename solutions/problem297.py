# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:

    def serialize(self, root) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""

        max_tree_depth = 0
        def get_max_tree_depth(root, depth):
            nonlocal max_tree_depth
            if root is None:
                return
            max_tree_depth = max(max_tree_depth, depth)
            get_max_tree_depth(root.left, depth + 1)
            get_max_tree_depth(root.right, depth + 1)

        get_max_tree_depth(root, 1)
        print(max_tree_depth)
        serialized_tree = []

        def traverse(root):
            if root is None:
                serialized_tree.append("#")
                return
            serialized_tree.append(str(root.val))
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return ",".join(serialized_tree)

        

    def deserialize(self, data) -> TreeNode:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return []
        list_tree = iter(data.split(','))
        
        def r_deserialize():
            val = next(list_tree)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = r_deserialize()
            node.right = r_deserialize()
            return node
        
        return r_deserialize()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))