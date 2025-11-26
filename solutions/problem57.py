class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        index = 0
        for interval in intervals:
            if newInterval[0] <= interval[0]:
                break
            index += 1
        if index == 0:
            intervals.insert(0, newInterval)
        elif index == len(intervals):
            intervals.append(newInterval)
        else:
            left_interval = False
            if intervals[index - 1][1] >= newInterval[0]:
                intervals[index - 1][1] = newInterval[1] #передвинули правую границу
                left_interval = True
            if intervals[index][0] <= newInterval[1]:
                if left_interval:
                    intervals[index - 1][1] = intervals[index][1]
                    intervals.pop(index)
                else:
                    intervals[index][0] = newInterval[0]
            if intervals[index - 1][1] < newInterval[0] and newInterval[1] < intervals[index][0]:
                intervals.insert(index, newInterval)
        print(index)
        return intervals

s = Solution()
print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))