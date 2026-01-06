# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        stack = self.iterate(root, dict(), 0)
        list_of_keys = sorted(list(stack.keys()))
        result = []
        for key in list_of_keys:
            result.append([])
            result[key] = stack[key]
        return result
    
    def iterate(self, root, stack, depth):
        if root is None:
            return stack
        if depth not in stack:
            stack[depth] = [root.val]
        else:
            if depth % 2 == 0:
                stack[depth].append(root.val)
            else:
                stack[depth].insert(0, root.val)
        stack = self.iterate(root.left, stack, depth + 1)
        stack = self.iterate(root.right, stack, depth + 1)
        return stack