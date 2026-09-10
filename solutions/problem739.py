from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        monotonic_stack = deque()
        answer = [0] * len(temperatures)
        for index, temperature in enumerate(temperatures):
            while monotonic_stack and monotonic_stack[-1][1] < temperature:
                index_ = monotonic_stack.pop()[0]
                answer[index_] = index - index_
            monotonic_stack.append((index, temperature))
        return answer

s = Solution()
print(s.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]))