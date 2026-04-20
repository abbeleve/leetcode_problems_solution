# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.maxSum = 0
        self.hash_map = {}
        self.total_amount = 0
        self.sumCounter(root)
        print(self.hash_map)
        keys = self.hash_map.keys()
        max_freq = 0
        res = []
        for key in keys:
            max_freq = max(max_freq, self.hash_map[key])
        for key in keys:
            if self.hash_map[key] == max_freq:
                res.append(key)
        return res

    def sumCounter(self, root):
        if root.left is None and root.right is None:
            self.hash_map[root.val] = self.hash_map.get(root.val, 0) + 1
            self.total_amount += 1
            return root.val
        left_sum, right_sum = 0, 0
        if root.left:
            left_sum = self.sumCounter(root.left)
        if root.right:
            right_sum = self.sumCounter(root.right)
        print(left_sum, right_sum, root.val)
        self.hash_map[left_sum + right_sum + root.val] = self.hash_map.get(left_sum + right_sum + root.val, 0) + 1
        self.total_amount += 1
        return left_sum + right_sum + root.val

s = Solution()
print(s.findFrequentTreeSum())