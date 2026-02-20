class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        self.word_exists = False
        self.board = board
        self.looking_word = word
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.search(board[i][j], i, j, [(i, j)]):
                        return True
        return False

    def search(self, word, i, j, history):
        if self.looking_word == word:
            self.word_exists = True
            return True
        
        for i, j in self.get_neighbors(i, j, history):
            if self.board[i][j] == self.looking_word[len(word)]:
                word += self.board[i][j]
                history.append((i, j))
                if self.search(word, i, j, history):
                    print(word)
                    return True
                word = word[:-1]
                history.pop()
        return False


    def get_neighbors(self, i, j, history):
        neighbors = []
        rows = len(self.board)
        cols = len(self.board[0])
        if i > 0 and (i - 1, j) not in history:
            neighbors.append((i - 1, j))
        if i < rows - 1 and (i + 1, j) not in history:
            neighbors.append((i + 1, j))
        if j > 0 and (i, j - 1) not in history:
            neighbors.append((i, j - 1))
        if j < cols - 1 and (i, j + 1) not in history:
            neighbors.append((i, j + 1))
        return neighbors
    
s = Solution()
print(s.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))