import heapq

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        self.matrix = matrix
        trie = [(0, 0)]
        if k == 1:
            return trie[0]
        stack = [(0, 0)]

        def get_neighbours(position: tuple):
            i, j = position[0], position[1]
            neighbours = []
            if i != 0:
                neighbours.append((i - 1, j))
            if i != len(self.matrix) - 1:
                neighbours.append((i + 1, j))
            if j != 0:
                neighbours.append((i, j - 1))
            if j != len(self.matrix[0]) - 1:
                neighbours.append((i, j + 1))
            return neighbours
    
        while len(stack) > 0:
            node = stack.pop(0)
            neighbours = get_neighbours(node)
            
        
s = Solution()
print(s.kthSmallest(matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8))