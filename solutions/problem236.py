# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        trace = self.lookForElement(root, p.val)
        trace2 = self.lookForElement(root, q.val)
        for node in trace[::-1]:
            if node in trace2:
                return node

    def lookForElement(self, root, lookup_element):
        if not root:
            return []
        
        stack = [(root, [root])]

        while stack:
            node, path = stack.pop()
            if node.val == lookup_element:
                return path

            if node.right:
                stack.append((node.right, path + [node.right]))
            if node.left:
                stack.append((node.left, path + [node.left]))