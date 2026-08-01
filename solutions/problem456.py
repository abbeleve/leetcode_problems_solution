from collections import deque

class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        stack = deque()
        deletion_happened = False
        for index in range(len(nums)):
            while stack and stack[-1] > nums[index]:
                stack.pop()
                deletion_happened = True
            if deletion_happened and stack:
                return True
            stack.append(nums[index])
            deletion_happened = False
        return False

s = Solution()
print(s.find132pattern(nums = [3,5,0,3,4]))