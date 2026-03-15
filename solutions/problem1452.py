class Solution:
    def constrainedSubsetSum(self, nums: list[int], k: int) -> int:
        stack = []
        dp = [nums[0]]
        for i in range(1, len(nums)):
            