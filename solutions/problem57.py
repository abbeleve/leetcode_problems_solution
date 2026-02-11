class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        first_elem = intervals[0][0]
        index = 0
        while index < len(intervals):
            interval = intervals[index]
            if newInterval[1] >= interval[1]:
                if newInterval[0] > interval[1]:
                    continue
                elif newInterval[0] >= interval[0] and newInterval[0] <= interval[0]:
                    first_elem = interval[0]
                intervals.pop(index)
            else:
                break
        if len(intervals) == 0:
            if first_elem <= newInterval[0]:
                intervals.append([first_elem, newInterval[1]])
                return intervals
            intervals.append(newInterval)
            return intervals
        if newInterval[1] >= intervals[0][0]:
            if newInterval[0] >= intervals[0][0]:
                return intervals
            else:
                intervals[0][0] = newInterval[0]
                return intervals
        else:
            intervals.insert(0, newInterval)
        return intervals

s = Solution()
print(s.insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))
