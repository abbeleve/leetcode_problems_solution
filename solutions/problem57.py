class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        left_border, right_border = newInterval[0], newInterval[1]
        left_index_save, right_index_save = 0, 0
        for left_index, interval in enumerate(intervals):
            if interval[1] >= left_border:
                left_index_save = left_index
                break
        for right_index, interval in enumerate(intervals):
            if interval[0] > right_border:
                right_index_save = right_index
                break
        if left_index_save == right_index_save:
            return intervals