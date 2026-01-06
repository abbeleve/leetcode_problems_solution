# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        stack = {}
        stack = self.iterate(root, stack, 0)
        list_of_keys = sorted(list(stack.keys()))
        result = []
        for key in list_of_keys:
            result.append(sum(stack[key])/len(stack[key]))
        return result

    def iterate(self, root, stack, depth):
        if root is None:
            return stack
        stack = self.iterate(root.left, stack, depth + 1)
        stack = self.iterate(root.right, stack, depth + 1)
        if depth not in stack:
            stack[depth] = [root.val]
        else:
            stack[depth].append(root.val)
        return stack