class Solution:
    def maxArea(self, height: list[int]) -> int:
        left_index = 0
        right_index = len(height) - 1
        max_area = 0
        while left_index <= right_index:
            area = min(height[left_index], height[right_index]) * (right_index - left_index)
            max_area = max(max_area, area)
            if height[left_index] >= height[right_index]:
                right_index -= 1
            else:
                left_index += 1
        return max_area

s = Solution()
print(s.maxArea([1,3,2,5,25,24,5]))
