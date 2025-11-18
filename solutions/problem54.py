class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        row_index = 0
        column_index = 0
        margin = 0
        result_sequence = []
        
        while len(matrix) >= 3 and len(matrix[0]) >= 3:
            first_row = matrix[0]
            result_sequence.extend(first_row)
            for row in range(1, len(matrix) - 1):
                result_sequence.append(matrix[row][-1]) 
                matrix.pop           
            last_row = matrix[-1::-1]
            result_sequence.extend(last_row)

            matrix.pop(0)
            matrix.pop()

            for row in range(0, len(matrix)):
                matrix[row].pop()
            
        if len(matrix) < 3 and len(matrix) > 0:
            if len(matrix) != 1:
                result_sequence.extend(matrix[0])
                result_sequence.extend(matrix[-1])
            else:
                result_sequence.extend(matrix[0])
            
        if len(matrix[0]) < 3 and len(matrix[0]) > 0:
            if len(matrix[0]) != 1:
                result_sequence.extend()
        

