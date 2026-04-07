class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        if len(grid) == 0:
            return grid[0][0]
        self.grid = grid
        infinite = 10**13
        self.optimal_grid = [[infinite for _ in range(len(grid[0]))] for __ in range(len(grid))]
        self.optimal_grid[0][0] = grid[0][0]
        track = set()
        time = grid[0][0]
        self.min_time = 10**13
        stack = [(0, 0)]
        while len(stack) > 0:
            node = stack.pop(0)
            track.add(node)
            neighbours = self.get_neighbours(node)
            for neighbour_node in neighbours:
                if neighbour_node in track:
                    continue
                stack.append(neighbour_node)
                if self.optimal_grid[neighbour_node[0]][neighbour_node[1]] == infinite:
                    self.optimal_grid[neighbour_node[0]][neighbour_node[1]] = max(self.grid[neighbour_node[0]][neighbour_node[1]], self.optimal_grid[node[0]][node[1]])
                else:
                    self.optimal_grid[neighbour_node[0]][neighbour_node[1]] = max(min(self.optimal_grid[neighbour_node[0]][neighbour_node[1]], self.optimal_grid[node[0]][node[1]]), self.grid[neighbour_node[0]][neighbour_node[1]])
        return self.optimal_grid[-1][-1]

    def get_neighbours(self, node):
        neighbours = []
        if node[0] != len(self.grid[0]) - 1:
            neighbours.append((node[0] + 1, node[1]))
        if node[0] != 0:
            neighbours.append((node[0] - 1, node[1]))
        if node[1] != len(self.grid) - 1:
            neighbours.append((node[0], node[1] + 1))
        if node[1] != 0:
            neighbours.append((node[0], node[1] - 1))
        neighbours.sort(key=lambda x: self.optimal_grid[x[0]][x[1]])
        return neighbours
    
s = Solution()
print(s.swimInWater([[0,3],[1,2]]))