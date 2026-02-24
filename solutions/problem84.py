class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_S = 0
        for index in range(len(heights)):
            while len(stack) > 0 and heights[index] < stack[0]:
                left_index = stack.pop(0)
                height = heights[left_index]
                width = index - left_index + 1
                max_S = max(max_S, width * height)

            stack.append(index)
    
s = Solution()
print(s.largestRectangleArea(heights=[2, 1, 5, 6, 2, 3]))