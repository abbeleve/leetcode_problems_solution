from collections import deque

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        self.mat = mat
        width, height = len(self.mat[0]), len(self.mat)
        self.dp = [[0]*width for _ in range(height)]
        self.hash_map = set()
        for i in range(height):
            for j in range(width):
                if self.mat[i][j] == 1:
                    self.dp[i][j] = float('inf')

        queue = deque()
        for i in range(height):
            for j in range(width):
                if self.mat[i][j] == 0:
                    start_node = (i, j)
                    queue.append(start_node)
                    self.hash_map.add(start_node)

        while queue:
            node = queue.popleft()
            i, j = node[0], node[1]
            neighbours = self.getNeighbours(node[0], node[1])
            for neighbour in neighbours:
                n_i, n_j = neighbour[0], neighbour[1]
                if (n_i, n_j) not in self.hash_map:
                    self.dp[n_i][n_j] = min(self.dp[n_i][n_j], self.dp[i][j] + 1)
                    queue.append(neighbour)
            self.hash_map.add(node)
        return self.dp

    def getNeighbours(self, i, j):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        width, height = len(self.mat[0]), len(self.mat)
        neighbors = []
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < height and 0 <= nj < width:
                neighbors.append((ni, nj))
                
        return neighbors
    
s = Solution()
print(s.updateMatrix(mat = [[0,0,0],[0,1,0],[0,0,0]]))