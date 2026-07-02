class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        i = 0
        amount_of_deletions = 0
        while i < len(intervals) - 1:
            if intervals[i + 1][1] <= intervals[i][1]:
                intervals.pop(i)
                amount_of_deletions += 1
                continue
            if intervals[i + 1][0] < intervals[i][1]:
                intervals.pop(i + 1)
                amount_of_deletions += 1
                continue
            if intervals[i][1] <= intervals[i + 1][0]:
                i += 1
        return amount_of_deletions

s = Solution()
print(s.eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]))