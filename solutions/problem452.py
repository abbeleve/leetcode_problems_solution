class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[0])
        index_points = 0
        while index_points < len(points) - 1:
            if points[index_points + 1][0] <= points[index_points][1]:
                if points[index_points + 1][1] <= points[index_points][1]:
                    points[index_points][0] = points[index_points + 1][0]
                    points[index_points][1] = points[index_points + 1][1]
                    points.pop(index_points + 1)
                else:
                    points[index_points][0] = points[index_points + 1][0]
                    points.pop(index_points + 1)
            else:
                index_points += 1
        return len(points)
    
s = Solution()
print(s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))