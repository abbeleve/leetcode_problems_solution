# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == key:
            if root.left is None and root.right is None:
                return None
            elif root.left is None and root.right is not None:
                return root.right
            elif root.right is None and root.left is not None:
                return root.left
            else:
                if root.right.left is None:
                    root.right.left = root.left
                    root = root.right
                else:
                    left_subtree = root.right.left
                    root.right.left = root.left
                    root = root.right
                    root_looking = root.left
                    while root_looking.right is not None:
                        root_looking = root_looking.right
                    root_looking.right = left_subtree
            return root
        look_up_root_node, look_up_node = self.lookupNode(root, key)
        if not(look_up_node):
            return root
        print(look_up_node)
        if look_up_node.left is None and look_up_node.right is None:
            if look_up_root_node.left == look_up_node:
                look_up_root_node.left = None
            if look_up_root_node.right == look_up_node:
                look_up_root_node.right = None
        elif look_up_node.left is not None and look_up_node.right is None:
            if look_up_root_node.left == look_up_node:
                look_up_root_node.left = look_up_node.left
            if look_up_root_node.right == look_up_node:
                look_up_root_node.right = look_up_node.left
        elif look_up_node.right is not None and look_up_node.left is None:
            if look_up_root_node.left == look_up_node:
                look_up_root_node.left = look_up_node.right
            if look_up_root_node.right == look_up_node:
                look_up_root_node.right = look_up_node.right
        else:
            if look_up_node.right.left is not None:
                if look_up_root_node.right == look_up_node:
                    look_up_root_node.right = look_up_node.right
                    left_subtree = look_up_node.right.left
                    look_up_node.right.left = look_up_node.left
                elif look_up_root_node.left == look_up_node:
                    look_up_root_node.left = look_up_node.right
                    left_subtree = look_up_node.right.left
                    look_up_node.right.left = look_up_node.left
                root_looking = look_up_node.left
                while root_looking.right is not None:
                    root_looking = root_looking.right
                root_looking.right = left_subtree
            else:
                if look_up_root_node.right == look_up_node:
                    look_up_root_node.right = look_up_node.right
                    look_up_node.right.left = look_up_node.left
                elif look_up_root_node.left == look_up_node:
                    look_up_root_node.left = look_up_node.right
                    look_up_node.right.left = look_up_node.left
        return root

    def lookupNode(self, root, key):
        stack = [root]
        while len(stack) > 0:
            node = stack.pop(0)
            if node.left:
                if node.left.val == key:
                    return node, node.left
                stack.append(node.left)
            if node.right:
                if node.right.val == key:
                    return node, node.right
                stack.append(node.right)
        return None, None