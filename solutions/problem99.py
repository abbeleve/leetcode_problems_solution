# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        self.tree_traverse = []
        self.traverse(root)
        for i in self.tree_traverse:
            print(i.val)
        first_deceiver, second_deceiver = None, None
        for index in range(len(self.tree_traverse) - 1):
            if self.tree_traverse[index].val < self.tree_traverse[index + 1].val:
                continue
            if first_deceiver is None:
                first_deceiver = index
            else:
                second_deceiver = index + 1
        print(first_deceiver, second_deceiver)
        if first_deceiver is not None and second_deceiver is not None:
            if first_deceiver == second_deceiver - 1:
                self.tree_traverse[first_deceiver].val, self.tree_traverse[second_deceiver + 1].val = self.tree_traverse[second_deceiver + 1].val, self.tree_traverse[first_deceiver].val
                print(root.val)
                return root
            self.tree_traverse[first_deceiver].val, self.tree_traverse[second_deceiver].val = self.tree_traverse[second_deceiver].val, self.tree_traverse[first_deceiver].val
            return root
        # print(first_deceiver, second_deceiver)
        second_deceiver = first_deceiver + 1
        self.tree_traverse[first_deceiver].val, self.tree_traverse[second_deceiver].val = self.tree_traverse[second_deceiver].val, self.tree_traverse[first_deceiver].val
        return root

    def traverse(self, root):
        if root is None:
            return
        self.traverse(root.left)
        self.tree_traverse.append(root)
        self.traverse(root.right)