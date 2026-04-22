class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        self.height, self.width = len(matrix), len(matrix[0])
        stack = [(0, 0)]
        hash_map = set()
        while len(stack) > 0:
            indexes = stack.pop()
            if indexes in hash_map:
                continue
            hash_map.add(indexes)
            i, j = indexes[0], indexes[1]
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                neighbours = self.getNeighbours(i, j, mode='bigger')
                for neighbour in neighbours:
                    stack.append(neighbour)
            if matrix[i][j] < target:
                neighbours = self.getNeighbours(i, j, mode='lesser')
                for neighbour in neighbours:
                    stack.append(neighbour)
        return False

    def getNeighbours(self, i, j, mode='None'):
        neighbours = []
        if mode == 'None':
            if i != 0:
                neighbours.append((i - 1, j))
            if i != self.height - 1:
                neighbours.append((i + 1, j))
            if j != 0:
                neighbours.append((i, j - 1))
            if j != self.width - 1:
                neighbours.append((i, j + 1))
        elif mode == 'lesser':
            if i != self.height - 1:
                neighbours.append((i + 1, j))
            if j != self.width - 1:
                neighbours.append((i, j + 1))
        elif mode == 'bigger':
            if i != 0:
                neighbours.append((i - 1, j))
            if j != 0:
                neighbours.append((i, j - 1))
        return neighbours

s = Solution()
print(s.searchMatrix([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], target = 19))