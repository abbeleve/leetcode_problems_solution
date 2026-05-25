class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        for i in range(len(intervals)):
            