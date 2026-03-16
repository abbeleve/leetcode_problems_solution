class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        events = []
        for start, end, height in buildings:
            events.append((start, 'START', height))
            events.append((end, 'END', height))
        events.sort(key=lambda x: x[0])
        result = []
        active_state = []
        current_max = 0
        for x, status, height in events:
            if status == 'START':
                active_state.append(height)
            else:
                active_state.pop(active_state.index(height))
            if len(active_state) > 0:
                max_height = max(active_state)
            else:
                max_height = 0
            if current_max != max_height:
                current_max = max_height
                result.append((x, current_max))
        return result

s = Solution()
print(s.getSkyline(buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))