import math

class Solution:
    def isBoomerang(self, points: list[list[int]]) -> bool:
        vector_1 = [points[1][0] - points[0][0], points[1][1] - points[0][1]]
        vector_2 = [points[2][0] - points[0][0], points[2][1] - points[0][1]]
        if vector_1 == [0, 0] or vector_2 == [0, 0]:
            return False
        cos = (vector_1[0]*vector_2[0] + vector_1[1]*vector_2[1])/(math.sqrt(vector_1[0]**2 + vector_1[1]**2) * math.sqrt(vector_2[0]**2 + vector_2[1]**2))
        print(cos)
        if 1 - 0.0000001 <= abs(cos) <= 1 + 0.0000001:
            return False
        return True

s = Solution()
print(s.isBoomerang(points = [[4,4],[9,9],[3,3]]))