from collections import deque

class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        self.grid = grid
        island_1 = set()
        starting_point = None
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 1:
                    starting_point = (i, j)
                    break
            if starting_point is not None:
                break
        queue.append(starting_point)
        island_1.add((i, j))
        while queue:
            i, j = queue.popleft()
            neighbours = self.get_neighbours(i, j)
            for neighbour in neighbours:
                if grid[neighbour[0]][neighbour[1]] == 1 and neighbour not in island_1:
                    island_1.add(neighbour)
                    queue.append(neighbour)
        queue = deque()
        range_grid = [[float('inf')] * len(grid) for _ in range(len(grid))]
        for node in list(island_1):
            queue.append(node)
            range_grid[node[0]][node[1]] = 0 
        res = float('inf')
        while queue:
            i, j = queue.popleft()
            neighbours = self.get_neighbours(i, j)
            for neighbour in neighbours:
                if neighbour in island_1:
                    continue
                if grid[neighbour[0]][neighbour[1]] == 1:
                    return range_grid[i][j]
                if range_grid[neighbour[0]][neighbour[1]] == float('inf'):
                    range_grid[neighbour[0]][neighbour[1]] = min(range_grid[neighbour[0]][neighbour[1]], range_grid[i][j] + 1)
                    queue.append((neighbour[0], neighbour[1]))
        return res

    def get_neighbours(self, i, j):
        h, w = len(self.grid), len(self.grid[0])
        neighbours = []

        if i > 0:
            neighbours.append((i - 1, j))
        if i < h - 1:
            neighbours.append((i + 1, j))
        if j > 0:
            neighbours.append((i, j - 1))
        if j < w - 1:
            neighbours.append((i, j + 1))

        return neighbours

s = Solution()
print(s.shortestBridge([[0,1,0],[0,0,0],[0,0,1]]))