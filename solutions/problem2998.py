from collections import deque

class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        if y >= x:
            return y - x
        queue = deque([(x, 0)])
        visited = {x}

        while queue:
            curr, steps = queue.popleft()
            if curr == y:
                return steps

            neighbours = [curr - 1, curr + 1]
            if curr % 11 == 0:
                neighbours.append(curr // 11)
            if curr % 5 == 0:
                neighbours.append(curr // 5)
            
            for neighbour in neighbours:
                if neighbour < 0 or neighbour > 10000:
                    continue
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour, steps + 1))
        return -1

s = Solution()
print(s.minimumOperationsToMakeEqual(x = 10000, y = 2))