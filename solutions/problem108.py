# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        mid_index = len(nums) // 2
        node = TreeNode(nums[mid_index])
        left_node = self.sortedArrayToBST(nums[0:mid_index])
        right_node = self.sortedArrayToBST(nums[mid_index + 1:])
        node.left = left_node
        node.right = right_node
        return node