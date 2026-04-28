class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    mat[i][j] = int('inf')
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    continue
                neighbours = self.getNeighbours(len(mat[0]), len(mat), i, j)
                minimum = int('inf')
                for y, x in neighbours:
                    

    def getNeighbours(self, width, height, i, j):
        neighbours = []
        if i == 0:
            neighbours.append((1, j))
        if i == height - 1:
            neighbours.append((height - 2, j))
        if j == 0:
            neighbours.append(i, 1)
        if j == width - 1:
            neighbours.append((i, width - 2))
        return neighbours