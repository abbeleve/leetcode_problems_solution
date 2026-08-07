# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        self.nums = nums
        
        return self.construct(0, len(self.nums))

    def construct(self, l, r):
        nums = self.nums
        if l == r:
            return None
        if r - l == 1:
            return TreeNode(val=nums[l])
        index_of_max_elem = l + nums[l:r].index(max(nums[l:r]))
        max_elem = nums[index_of_max_elem]
        new_node = TreeNode(max_elem, self.construct(l, index_of_max_elem), self.construct(index_of_max_elem + 1, r))
        return new_node