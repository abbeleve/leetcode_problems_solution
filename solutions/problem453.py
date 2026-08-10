class Solution:
    def minMoves(self, nums: list[int]) -> int:
        minimal_element = min(nums)
        for i in range(len(nums)):
            nums[i] = nums[i] - minimal_element
        return sum(nums)