import math
import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        hash_map = {}
        distances = []
        for x, y in points:
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(distances, distance)
            if distance in hash_map:
                hash_map[distance].append((x, y))
            else:
                hash_map[distance] = [(x, y)]
        closest = heapq.nsmallest(k, distances)
        res = []
        for point_distance in closest:
            res.append(list(hash_map[point_distance].pop()))
        return res

s = Solution()
print(s.kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2))