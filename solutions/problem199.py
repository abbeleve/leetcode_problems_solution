# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        stack = self.iterate(root, dict(), 0)
        list_of_keys = sorted(list(stack.keys()))
        result = []
        for key in list_of_keys:
            result.append(stack[key]['value'])
        return result
    
    def iterate(self, root, stack, depth):
        if root is None:
            return stack
        stack = self.iterate(root.left, stack, depth + 1)
        stack = self.iterate(root.right, stack, depth + 1)
        if depth not in stack:
            stack[depth] = {}
            # stack[depth]['rightness'] = rightness
            stack[depth]['value'] = root.val
        else:
            # if stack[depth]['rightness'] < rightness:
            stack[depth]['value'] = root.val
        return stack