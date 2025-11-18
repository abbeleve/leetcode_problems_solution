class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for row in board:
            row_info = []
            for row_elem in row:
                if row_elem in row_info:
                    return False
                if row_elem != '.':
                    row_info.append(row_elem)
        
        for column_index in range(len(board)):
            column_info = []
            for column_elem_index in range(len(board)):
                column_elem = board[column_elem_index][column_index]
                if column_elem in column_info:
                    return False
                if column_elem != '.':
                    column_info.append(column_elem)
                
        for row_index in range(0, len(board), 3):
            for column_index in range(0, len(board), 3):
                table_info = []
                for table_row_index in range(row_index, row_index + 3):
                    for table_column_index in range(column_index, column_index + 3):
                        if board[table_row_index][table_column_index] in table_info:
                            return False
                        if board[table_row_index][table_column_index] != '.':
                            table_info.append(board[table_row_index][table_column_index])

        return True

s = Solution()
print(s.isValidSudoku(board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
