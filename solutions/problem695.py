from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        ones_indexes = set()
        w, h = len(grid[0]), len(grid)
        res = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    ones_indexes.add((i, j))
        while len(ones_indexes) > 0:
            one_index = ones_indexes.pop()
            queue = deque()
            queue.append(one_index)
            sum = 0
            while queue:
                node = queue.popleft()
                sum += 1
                neighbours = self.get_neighbours(node[0], node[1], w, h)
                for i, j in neighbours:
                    if (i, j) in ones_indexes:
                        ones_indexes.remove((i, j))
                        queue.append((i, j))
            res = max(res, sum)
        return res

    def get_neighbours(self, i, j, w, h):
        neighbours = []
        if i != 0:
            neighbours.append((i - 1, j))
        if i != h - 1:
            neighbours.append((i + 1, j))
        if j != 0:
            neighbours.append((i, j - 1))
        if j != w - 1:
            neighbours.append((i, j + 1))
        return neighbours