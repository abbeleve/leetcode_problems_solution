from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        self.grid = grid
        res = 0
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        while queue:
            i, j, minute = queue.popleft()
            neighbours = self.get_neighbours(i, j)
            for neighbour in neighbours:
                nei_i, nei_j = neighbour
                if grid[nei_i][nei_j] == 2 or grid[nei_i][nei_j] == 0:
                    continue
                queue.append((nei_i, nei_j, minute + 1))
                grid[nei_i][nei_j] = 2
                res = max(res, minute + 1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return res

    def get_neighbours(self, i, j):
        neighbours = []
        if i != 0:
            neighbours.append((i - 1, j))
        if j != 0:
            neighbours.append((i, j - 1))
        if i != len(self.grid) - 1:
            neighbours.append((i + 1, j))
        if j != len(self.grid[0]) - 1:
            neighbours.append((i, j + 1))
        return neighbours