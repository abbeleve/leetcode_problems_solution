class TreeNode:
    def __init__(self, letter: str):
        self.letter = letter
        self.nodes = {}

class WordDictionary:

    def __init__(self):
        self.root = TreeNode('')

    def addWord(self, word: str) -> None:
        pointer = self.root
        for index, letter in enumerate(word):
            if index == len(word) - 1:
                letter = letter + "*"
            if letter not in pointer.nodes:
                pointer.nodes[letter] = TreeNode(letter)
            pointer = pointer.nodes[letter]

    def search(self, word: str) -> bool:
        pointer = self.root
        queue = []
        for letter in word:
            if letter == ".":
                for node in pointer.nodes:
                    queue.append(node)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)