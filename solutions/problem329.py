class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        self.matrix = matrix
        self.memo = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        max_path = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                current_len = self.dfs((i, j))
                max_path = max(max_path, current_len)
        return max_path

    def dfs(self, index: tuple):
        i, j = index[0], index[1]
        if self.memo[i][j] != 0:
            return self.memo[i][j]
        neighbours = self.get_neighbours(index)
        depth = 1
        for neighbour in neighbours:
            if self.matrix[neighbour[0]][neighbour[1]] > self.matrix[i][j]:
                current_neighbour_path = 1 + self.dfs((neighbour[0], neighbour[1]))
                depth = max(depth, current_neighbour_path)
        
        self.memo[i][j] = depth
        return depth

    def get_neighbours(self, index: tuple):
        neighbours = []
        i, j = index[0], index[1]
        if i != 0:
            neighbours.append((i - 1, j))
        if i != len(self.matrix) - 1:
            neighbours.append((i + 1, j))
        if j != 0:
            neighbours.append((i, j - 1))
        if j != len(self.matrix[0]) - 1:
            neighbours.append((i, j + 1))
        return neighbours