from collections import deque

class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        stack = deque()
        hash_map = {}
        for i in range(len(nums)):
            while stack:
                if nums[stack[-1]] <= nums[i]:
                    index = stack.pop()
                    hash_map[index] = i