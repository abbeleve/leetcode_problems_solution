class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        time_points_int = [list(map(lambda x: int(x), i.split(':'))) for i in timePoints]
        time_points_int.sort(key=lambda x: (x[0], x[1]))
        minimal_diff = float('inf')
        max_diff = 24 * 60
        for i in range(len(time_points_int) - 1):
            hours = time_points_int[i + 1][0] - time_points_int[i][0]
            minutes = time_points_int[i + 1][1] - time_points_int[i][1]
            res = hours * 60 + minutes
            if hours >= 12:
                res = max_diff - res
            minimal_diff = min(minimal_diff, res)
        last_diff = abs((time_points_int[-1][0] - time_points_int[0][0]) * 60 + time_points_int[-1][1] - time_points_int[0][1])
        minimal_diff = min(minimal_diff, last_diff, max_diff - last_diff)
        return minimal_diff

s = Solution()
print(s.findMinDifference(timePoints = ["23:59","00:00"]))