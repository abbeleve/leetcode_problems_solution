from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        result = []
        monotonic_stack = deque()
        for i in range(len(nums)):
            if i < k:
                while len(monotonic_stack) > 0 and nums[i] > nums[monotonic_stack[-1]]:
                    monotonic_stack.pop()
                monotonic_stack.append(i)
                if i == k - 1:
                    result.append(nums[monotonic_stack[0]])
                continue
            if i > monotonic_stack[0] + k - 1:
                monotonic_stack.popleft()
            print(i)
            while len(monotonic_stack) > 0 and nums[i] > nums[monotonic_stack[-1]]:
                monotonic_stack.pop()
            monotonic_stack.append(i)
            result.append(nums[monotonic_stack[0]])
        return result
    
s = Solution()
print(s.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))