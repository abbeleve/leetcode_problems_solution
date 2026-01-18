class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        left, right = 0, len(nums) - 1
        