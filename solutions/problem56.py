class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        interval_index = 0
        while interval_index < len(intervals) - 1:
            if intervals[interval_index][1] >= intervals[interval_index + 1][0]:
                if intervals[interval_index][1] >= intervals[interval_index + 1][1]:
                    intervals.pop(interval_index + 1)
                else:
                    intervals[interval_index][1] = intervals[interval_index + 1][1]
                    intervals.pop(interval_index + 1)
            else:
                interval_index += 1
        return intervals
    
s = Solution()
print(s.merge([[4,7],[1,4]]))