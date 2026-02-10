class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        if len(points) == 1:
            return 1
        inf = 10**19
        longest_line_length = 2
        for i in range(len(points)):
            point_i = points[i]
            slope, slope_ = None, None
            for j in range(i + 1, len(points)):
                point_j = points[j]
                line_length = 2
                if point_j[0] == point_i[0]:
                    slope = inf
                else:
                    slope = abs((point_j[1] - point_i[1]) / (point_j[0] - point_i[0]))
                for z in range(len(points)):
                    point_z = points[z]
                    if z == i or z == j:
                        continue
                    if point_z[0] == point_i[0]:
                        slope_ = inf
                    else:
                        slope_ = abs((point_z[1] - point_i[1]) / (point_z[0] - point_i[0]))
                    if slope_ == slope:
                        line_length += 1
                        longest_line_length = max(longest_line_length, line_length)

        return longest_line_length

s = Solution()
print(s.maxPoints(points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))