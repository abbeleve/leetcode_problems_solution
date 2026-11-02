class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        stops = []
        for trip in trips:
            capacity -= trip[0]
            stops.append((trip[2], trip[0]))
            i = 0
            while i < len(stops):
                stop = stops[i]
                if trip[1] >= stop[0]:
                    capacity += stop[1]
                    stops.remove(stop)
                else:
                    i += 1
            if capacity < 0:
                return False
        return True

s = Solution()
print(s.carPooling([[3,2,8],[4,4,6],[10,8,9]], 11))