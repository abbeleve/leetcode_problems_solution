class TreeNode:
    def __init__(self, letter: str):
        self.letter = letter
        self.nodes = {}

class Trie:

    def __init__(self):

        self.root = TreeNode('')

    def insert(self, word: str) -> None:
        pointer = self.root
        for index, letter in enumerate(word):
            if index == len(word) - 1:
                letter = letter + "*"
            if letter not in pointer.nodes:
                pointer.nodes[letter] = TreeNode(letter)
            pointer = pointer.nodes[letter]
        
        

    def search(self, word: str) -> bool:
        pointer = self.root
        for index, letter in enumerate(word):
            if index == len(word) - 1:
                letter = letter + "*"
            if letter not in pointer.nodes:
                return False
            pointer = pointer.nodes[letter]
        return True

    def startsWith(self, prefix: str) -> bool:
        pointer = self.root
        for index, letter in enumerate(prefix):
            if index == len(prefix) - 1:
                if letter in pointer.nodes or letter + "*" in pointer.nodes:
                    return True
                return False
            if letter not in pointer.nodes:
                return False
            pointer = pointer.nodes[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)