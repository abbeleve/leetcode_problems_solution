class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        matrix = self.transpose(matrix)
        matrix = self.swap_verticles(matrix)
        return matrix
        
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        length_matrix = len(matrix)
        for row_index in range(length_matrix - 1):
            for inner_index in range(row_index + 1, length_matrix):
                save = matrix[row_index][inner_index]
                matrix[row_index][inner_index] = matrix[inner_index][row_index]
                matrix[inner_index][row_index] = save

        return matrix
    
    def swap_verticles(self, matrix: list[list[int]]) -> list[list[int]]:
        length_matrix = len(matrix)
        for verticles_index in range(length_matrix // 2):
            last_verticles_index = length_matrix - (verticles_index + 1)
            for index in range(length_matrix):
                save = matrix[index][verticles_index]
                matrix[index][verticles_index] = matrix[index][last_verticles_index]
                matrix[index][last_verticles_index] = save

        return matrix
    
s = Solution()
print(s.rotate([[1,2,3],[4,5,6],[7,8,9]]))