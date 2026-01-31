from collections import deque

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        for i in range(len(board)):
            elem = board[i][0]
            if elem == 'O':
                self.bfs(board, i, 0)
            elem = board[i][len(board[0]) - 1]
            if elem == 'O':
                self.bfs(board, i, len(board[0]) - 1)
        
        for j in range(len(board[0])):
            elem = board[0][j]
            if elem == 'O':
                self.bfs(board, 0, j)
            elem = board[len(board) - 1][j]
            if elem == 'O':
                self.bfs(board, len(board) - 1, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                elem = board[i][j]
                if elem == 'O':
                    board[i][j] = 'X'
                if elem == '#':
                    board[i][j] = 'O'

    def bfs(self, board, i, j):
        query = [(i, j)]
        while len(query) > 0:
            i, j = query.pop(0)
            board[i][j] = '#'
            if i - 1 >= 0:
                if board[i - 1][j] == 'O':
                    query.append((i - 1, j))
                    board[i - 1][j] = '#'
            if i + 1 < len(board):
                if board[i + 1][j] == 'O':
                    query.append((i + 1, j))
                    board[i + 1][j] = '#'
            if j - 1 >= 0:
                if board[i][j - 1] == 'O':
                    query.append((i, j - 1))
                    board[i][j - 1] = '#'
            if j + 1 < len(board[0]):
                if board[i][j + 1] == 'O':
                    query.append((i, j + 1))
                    board[i][j + 1] = '#'
        
s = Solution()
print(s.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))