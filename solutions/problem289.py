class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        next_board = []
        for height, row_list in enumerate(board):
            inside_next_board = []
            for row_index, row_elem in enumerate(row_list):
                alive_around = 0
                if row_index != len(row_list) - 1:
                    alive_around += row_list[row_index + 1]
                if row_index != 0:
                    alive_around += row_list[row_index - 1]
                if height != len(board) - 1:
                    alive_around += board[height + 1][row_index]
                if height != 0:
                    alive_around += board[height - 1][row_index]
                if height != len(board) - 1 and row_index != len(row_list) - 1:
                    alive_around += board[height + 1][row_index + 1]
                if height != len(board) - 1 and row_index != 0:
                    alive_around += board[height + 1][row_index - 1]
                if height != 0 and row_index != len(row_list) - 1:
                    alive_around += board[height - 1][row_index + 1]
                if height != 0 and row_index != 0:
                    alive_around += board[height - 1][row_index - 1]
                if row_elem == 1:
                    if alive_around < 2:
                        inside_next_board.append(0)
                    elif 2 <= alive_around <= 3:
                        inside_next_board.append(1)
                    elif alive_around > 3:
                        inside_next_board.append(0)
                else:
                    if alive_around == 3:
                        inside_next_board.append(1)
                    else:
                        inside_next_board.append(0)
                print(f"Для {height, row_index}, Соседи: {alive_around}")
            next_board.append(inside_next_board)
        for height, row_list in enumerate(next_board):
            for row_index, row_elem in enumerate(row_list):
                board[height][row_index] = next_board[height][row_index]

s = Solution()
board=[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
s.gameOfLife(board)
print(board)