# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None:
            return 1
        if root.right is None:
            return 2
        amount_of_nodes = 0
        left_depth = 0
        save_root = root
        while root.left:
            amount_of_nodes += 2**left_depth
            root = root.left
            left_depth += 1
        print(amount_of_nodes)
        root = save_root
        depth = 0
        while root.left:
            left_node_ending, right_depth = self.checkRight(root, depth, left_depth)
            print(left_node_ending, right_depth)
            if depth == left_depth - 1:
                if left_node_ending:
                    return amount_of_nodes + 1
            if left_depth == right_depth:
                offset = 1 if left_node_ending else 0
                amount_of_nodes += 2**(left_depth-depth-offset) + offset
                return amount_of_nodes
            root = root.left
            depth += 1

        return amount_of_nodes

    def checkRight(self, root, right_depth, left_depth):
        # depth_save = right_depth
        while root.right:
            root = root.right
            right_depth += 1
            if root.left and root.right is None:
                right_depth += 1
                return True, right_depth
        # if left_depth == right_depth:
        #     return False, right_depth
        if root.left:
            right_depth += 1
            return True, right_depth
        return False, right_depth