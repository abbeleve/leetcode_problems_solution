class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        zero_indexes = []
        for row_index in range(len(matrix)):
            for column_index in range(len(matrix[row_index])):
                if matrix[row_index][column_index] == 0:
                    zero_indexes.append((row_index, column_index))

        for zero_row, zero_column in zero_indexes:
            for column in range(len(matrix[zero_row])):
                matrix[zero_row][column] = 0
            for row in range(len(matrix)):
                matrix[row][zero_column] = 0
        return matrix
    
s = Solution()
print(s.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))